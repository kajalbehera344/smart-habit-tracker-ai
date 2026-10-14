from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import date, timedelta
import os

app = Flask(__name__)
os.makedirs(app.instance_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'habits.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
analyzer = SentimentIntensityAnalyzer()

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(40), default='Personal')
    color = db.Column(db.String(20), default='#8b7cf6')

class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    log_date = db.Column(db.Date, nullable=False, default=date.today)
    completed = db.Column(db.Boolean, default=True)
    __table_args__ = (db.UniqueConstraint('habit_id', 'log_date', name='unique_habit_day'),)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_date = db.Column(db.Date, default=date.today, nullable=False)
    text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float, nullable=False)

def serialize_habit(h):
    log = HabitLog.query.filter_by(habit_id=h.id, log_date=date.today()).first()
    week_start = date.today() - timedelta(days=6)
    done = HabitLog.query.filter(HabitLog.habit_id == h.id, HabitLog.log_date >= week_start, HabitLog.completed.is_(True)).count()
    return {'id': h.id, 'name': h.name, 'category': h.category, 'color': h.color, 'done_today': bool(log and log.completed), 'weekly_done': done}

def streak_count():
    count, day = 0, date.today()
    while HabitLog.query.filter_by(log_date=day, completed=True).count() > 0:
        count += 1
        day -= timedelta(days=1)
    return count

def seed():
    if Habit.query.count() == 0:
        db.session.add_all([Habit(name='Drink 8 glasses of water', category='Health', color='#5ba9e8'), Habit(name='Read for 15 minutes', category='Learning', color='#a78bfa'), Habit(name='Take a mindful break', category='Wellbeing', color='#f4a261')])
        db.session.commit()

with app.app_context():
    db.create_all()
    seed()

@app.route('/')
def index(): return render_template('index.html')

@app.get('/api/health')
def health(): return jsonify({'status':'ok','app':'Smart Habit Tracker AI'})

@app.get('/api/dashboard')
def dashboard():
    today = date.today()
    habits = Habit.query.order_by(Habit.id.desc()).all()
    completed = HabitLog.query.filter_by(log_date=today, completed=True).count()
    labels, values = [], []
    for offset in range(6, -1, -1):
        d = today - timedelta(days=offset)
        labels.append(d.strftime('%a'))
        values.append(HabitLog.query.filter_by(log_date=d, completed=True).count())
    entries = JournalEntry.query.order_by(JournalEntry.id.desc()).limit(6).all()
    return jsonify({'habits':[serialize_habit(h) for h in habits], 'stats':{'total':len(habits),'completed':completed,'rate':round(completed/len(habits)*100) if habits else 0,'streak':streak_count()}, 'chart':{'labels':labels,'values':values}, 'journal':[{'id':e.id,'date':e.entry_date.isoformat(),'text':e.text,'sentiment':e.sentiment} for e in entries]})

@app.post('/api/habits')
def add_habit():
    data = request.get_json(silent=True) or {}
    name = (data.get('name') or '').strip()
    if not name: return jsonify({'error':'Please enter a habit name.'}), 400
    if len(name) > 100: return jsonify({'error':'Habit name must be 100 characters or fewer.'}), 400
    h = Habit(name=name, category=(data.get('category') or 'Personal')[:40], color=data.get('color') or '#8b7cf6')
    db.session.add(h); db.session.commit()
    return jsonify(serialize_habit(h)), 201

@app.post('/api/habits/<int:habit_id>/toggle')
def toggle_habit(habit_id):
    h = db.session.get(Habit, habit_id)
    if not h: return jsonify({'error':'Habit not found.'}), 404
    log = HabitLog.query.filter_by(habit_id=habit_id, log_date=date.today()).first()
    if log: log.completed = not log.completed
    else: db.session.add(HabitLog(habit_id=habit_id, log_date=date.today(), completed=True))
    db.session.commit()
    return jsonify({'ok':True,'habit':serialize_habit(h)})

@app.delete('/api/habits/<int:habit_id>')
def delete_habit(habit_id):
    h = db.session.get(Habit, habit_id)
    if not h: return jsonify({'error':'Habit not found.'}), 404
    HabitLog.query.filter_by(habit_id=habit_id).delete(); db.session.delete(h); db.session.commit()
    return jsonify({'ok':True})

@app.post('/api/ai/reflect')
def reflect():
    data = request.get_json(silent=True) or {}
    text = (data.get('text') or '').strip()
    if not text: return jsonify({'error':'Write a little about your day first.'}), 400
    if len(text) > 3000: return jsonify({'error':'Keep your reflection under 3,000 characters.'}), 400
    score = analyzer.polarity_scores(text)['compound']
    if score >= .25:
        mood, emoji, advice = 'Positive', '🌞', 'You seem to be having a positive day. Notice what helped, and choose one small win to repeat tomorrow.'
    elif score <= -.25:
        mood, emoji, advice = 'Low', '🌧️', 'Today may have felt heavy. Try one manageable task, a short break, or reaching out to someone you trust.'
    else:
        mood, emoji, advice = 'Balanced', '🌿', 'Your reflection sounds fairly balanced. A short walk, some water, or ten focused minutes on a priority could help you reset.'
    entry = JournalEntry(text=text, sentiment=mood, score=score)
    db.session.add(entry); db.session.commit()
    return jsonify({'sentiment':mood,'emoji':emoji,'score':round(score,3),'advice':advice})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
