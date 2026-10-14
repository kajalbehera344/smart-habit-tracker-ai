# Smart Habit Tracker AI 🌱

A responsive habit-tracking web app built with Flask, SQLite, vanilla JavaScript, Chart.js, and VADER sentiment analysis.

## Features
- Dashboard with daily completion percentage, habit count, streak, and weekly activity chart
- Add, complete/uncomplete, and delete habits
- Habit categories and colors
- AI-assisted daily reflection: sentiment estimate, score, and supportive suggestion
- SQLite storage for habits, check-ins, and journal entries
- Dark/light theme toggle and responsive layout
- REST API and `/api/health` endpoint

> The sentiment analyzer is a lightweight text sentiment estimate, not a mental-health assessment or diagnosis. Reflections are stored locally in `instance/habits.db`.

## Run on Windows
1. Extract the ZIP and open this folder in VS Code.
2. Double-click `run_windows.bat`, or use the VS Code terminal:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python app.py
   ```
3. Open http://127.0.0.1:5000 in your browser.

If PowerShell blocks activation, use `run_windows.bat` or run `.venv\\Scripts\\python.exe -m pip install -r requirements.txt`, then `.venv\\Scripts\\python.exe app.py`.

## macOS/Linux
Run `chmod +x run_mac_linux.sh && ./run_mac_linux.sh`, then open http://127.0.0.1:5000.

## API endpoints
- `GET /api/health` — health check
- `GET /api/dashboard` — habits, statistics, chart data, and recent journal entries
- `POST /api/habits` — JSON `{ "name": "Stretch", "category": "Health", "color": "#8b7cf6" }`
- `POST /api/habits/<id>/toggle` — toggle today's completion
- `DELETE /api/habits/<id>` — remove a habit
- `POST /api/ai/reflect` — JSON `{ "text": "I finished my work and feel good." }`


```
