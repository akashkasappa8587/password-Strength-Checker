# Password Strength UI + Backend

This project pairs a static HTML UI (`Password.html`) with a small Flask backend (`app.py`) that provides two endpoints:

- `POST /api/check` — accepts JSON { password: string } and returns JSON { score, label, feedback }
- `GET /api/generate` — returns a generated password JSON { password }

Quick start (Windows PowerShell)

1. Install dependencies (once):

```powershell
C:/Users/DELL/Desktop/Password/.venv/Scripts/python.exe -m pip install -r C:/Users/DELL/Desktop/Password/requirements.txt
```

2. Start the app and open the UI (one-liner):

```powershell
C:/Users/DELL/Desktop/Password/run.ps1
```

This will open a new PowerShell window that runs the Flask dev server and will open your browser to `http://127.0.0.1:5000/`.

3. Manual start (alternative):

```powershell
C:/Users/DELL/Desktop/Password/.venv/Scripts/python.exe C:/Users/DELL/Desktop/Password/app.py
# then open http://127.0.0.1:5000/ in your browser
```

4. Quick API test (PowerShell):

```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/api/check' -Method POST -ContentType 'application/json' -Body '{"password":"StrongP@ss1"}' | ConvertTo-Json -Depth 3
```

If you see connectivity issues when calling the endpoint from a separate process or browser, run the included `test_local.py` which uses Flask's test client (no network required):

```powershell
C:/Users/DELL/Desktop/Password/.venv/Scripts/python.exe C:/Users/DELL/Desktop/Password/test_local.py
```

Notes
- `Password.py` is still usable as a standalone interactive checker.
- `app.py` imports `check_password_strength` from `Password.py`. If that import fails, `app.py` contains a fallback checker.

If you'd like I can add:
- A CLI mode to `Password.py` so you can call `Password.py --password "..."` non-interactively
- A PowerShell wrapper that installs deps and runs everything with one command
