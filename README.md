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

Live Demo: https://smart-habit-tracker-ai.onrender.com
GitHub Repository: https://github.com/kajalbehera344/smart-habit-tracker-ai

```

## Latest Update
README documentation updated.

## Project Status
Smart Habit Tracker AI is deployed and available online.
