# TEAM RCS Demo Prototype

## Features in this student demo
- Emergency report form with incident categories
- Language selection: English, Telugu and Hindi
- Browser speech-to-text input (browser/service support varies)
- GPS location capture with browser permission
- Offline report queue using localStorage and sync attempt on reconnect
- Rule-based High / Medium / Low priority classification (not trained AI)
- Simulated nearest-patrol suggestion using fictional sample patrol coordinates
- Recent reports list

## Important limitations
This is a demonstration only. It does not contact 112, police, or a control room. Patrol data is fictional. Priority labels use simple keyword rules, not a trained AI model. Reports are stored in server memory and disappear when the server restarts. Do not use this demo to request real emergency help. In India, call 112 for emergencies.

## Run on Windows / VS Code
1. Install Python 3.10+.
2. Open this folder in VS Code.
3. In the terminal run:
   `python -m venv venv`
4. Activate:
   `venv\\Scripts\\activate`
5. Install:
   `pip install -r requirements.txt`
6. Start:
   `python app.py`
7. Open `http://127.0.0.1:5000` in Chrome.

GPS and microphone require browser permission. GPS works on localhost. Browser speech recognition may require an internet connection.

## Folder structure
- app.py — Flask backend and demo API
- templates/index.html — interface
- static/style.css — styling
- static/app.js — voice, GPS, offline queue and API calls
- requirements.txt — Python dependency
