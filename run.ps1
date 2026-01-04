# Quick runner for the Password project (Windows PowerShell)
# Starts the Flask server in a new PowerShell window and opens the UI in the default browser.

$python = 'C:/Users/DELL/Desktop/Password/.venv/Scripts/python.exe'
$app = 'C:/Users/DELL/Desktop/Password/app.py'

Write-Output "Starting Password app using: $python $app"

# Launch a new PowerShell window that keeps running (so you can see logs)
Start-Process -FilePath 'powershell.exe' -ArgumentList "-NoExit", "-Command", "& '$python' '$app'"

# Give the server a second to start, then open the browser
Start-Sleep -Seconds 1
Start-Process 'http://127.0.0.1:5000/'

Write-Output "Done. If the browser doesn't load, open http://127.0.0.1:5000/ manually."
