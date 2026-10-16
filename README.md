🌱 Smart Habit Tracker AI

An interactive and responsive habit-tracking web application built with Python, Flask, SQLite, JavaScript, Chart.js, and VADER Sentiment Analysis. The application helps users build consistent routines, monitor daily progress, track streaks, and reflect on their mood through AI-assisted sentiment analysis.

🚀 Live Demo

Live Application: https://smart-habit-tracker-ai.onrender.com

GitHub Repository: https://github.com/kajalbehera344/smart-habit-tracker-ai

✨ Features

✅ Interactive Dashboard — View daily completion percentage, total habits, current streak, and weekly activity.

✅ Habit Management — Add, complete, uncomplete, and delete habits.

🎨 Habit Categories — Organize habits using categories and custom colors.

🤖 AI-Assisted Daily Reflection — Analyze journal entries using VADER sentiment analysis and receive supportive suggestions.

📊 Sentiment Score — Display an estimated sentiment score based on written reflections.

📈 Weekly Activity Chart — Visualize habit completion and consistency using Chart.js.

📝 Journal Storage — Store daily reflections, habits, and check-ins using SQLite.

🌙 Dark and Light Themes — Switch between themes for a comfortable user experience.

📱 Responsive Interface — Access the application on desktop and mobile screens.

🔌 REST API — Handle habit operations, dashboard data, and daily reflections through Flask API endpoints.

🛠️ Tech Stack

🐍 Python — Core application logic

🌐 Flask — Backend framework and REST API

🗄️ SQLite — Local database storage

🎨 HTML5 and CSS3 — User interface and styling

⚡ JavaScript — Frontend interactions

📊 Chart.js — Dashboard visualizations

🤖 VADER Sentiment Analysis — Text sentiment estimation

🔗 Git and GitHub — Version control and source code management

☁️ Render — Application deployment

📂 Project Structure

```text
smart-habit-tracker-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── run_windows.bat
├── run_mac_linux.sh
├── templates/
├── static/
└── instance/
    └── habits.db
```

📌 The folder structure may vary depending on your project files. The database is typically created locally when the application initializes.

⚙️ Installation and Setup

📋 Prerequisites

✅ Python 3.10 or a compatible version

✅ Git

✅ Visual Studio Code or another code editor

💻 Step 1: Clone the Repository

```bash
git clone https://github.com/kajalbehera344/smart-habit-tracker-ai.git
cd smart-habit-tracker-ai
```

🐍 Step 2: Create a Virtual Environment

Windows PowerShell:

```powershell
py -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

📦 Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

🚀 Step 4: Run the Application

```bash
python app.py
```

🌐 Step 5: Open in Your Browser

Visit: http://127.0.0.1:5000

💡 Windows alternative: Run `run_windows.bat` from the project directory.

🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check application health |
| GET | `/api/dashboard` | Retrieve dashboard statistics and recent journal entries |
| POST | `/api/habits` | Create a new habit |
| POST | `/api/habits/<id>/toggle` | Toggle today's habit completion |
| DELETE | `/api/habits/<id>` | Delete a habit |
| POST | `/api/ai/reflect` | Analyze a daily reflection |

📝 Example: Create a Habit

```json
{
  "name": "Morning Exercise",
  "category": "Health",
  "color": "#8b7cf6"
}
```

📌 The API expects JSON where applicable. Request fields and responses depend on the implementation in `app.py`.

🤖 How AI-Assisted Reflection Works

1. 📝 The user writes a short daily reflection.
2. 🔍 VADER analyzes the text and estimates its sentiment.
3. 📊 The application derives a sentiment score from the analysis.
4. 💬 A supportive suggestion is displayed based on the estimated sentiment.

⚠️ Sentiment analysis is a lightweight text-based estimate. It is not a mental-health assessment or diagnosis, nor a substitute for professional support.

🔒 Data Storage and Privacy

🔹 Habit records, check-ins, and journal entries are stored in SQLite.

🔹 The local database is typically located at `instance/habits.db`.

🔹 In the deployed application, database persistence depends on the hosting environment and its storage configuration.

🔹 Avoid storing passwords, API keys, or other sensitive information in source code or public repositories.

🌐 Deployment

☁️ The application is deployed on Render.

🔗 Live URL: https://smart-habit-tracker-ai.onrender.com

💡 Free hosting services may put inactive applications to sleep, so the first request after inactivity may take longer to load.

🔮 Future Improvements

🔔 Habit reminders and notification support

👤 User authentication and personalized accounts

📅 Monthly reports and advanced progress analytics

🎯 Habit recommendations based on completion patterns

📄 Exportable progress reports

🗄️ Persistent production database configuration

👩‍💻 Author

Kajal Behera

🔗 GitHub: https://github.com/kajalbehera344

📄 License

This project is available for educational and personal portfolio purposes. Add a `LICENSE` file if you intend to distribute it under a specific open-source license.
