from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
import secrets, string

app = Flask(__name__, static_folder='.')

HERE = Path(__file__).parent

try:
    # Import the check_password_strength function from Password.py
    from Password import check_password_strength
except Exception:
    # If import fails, provide a fallback implementation
    def check_password_strength(password):
        score = 0
        feedback = []
        if len(password) >= 8:
            score += 2
            feedback.append(f"Length OK ({len(password)})")
        if any(c.isupper() for c in password):
            score += 1
            feedback.append("Has uppercase")
        if any(c.islower() for c in password):
            score += 1
            feedback.append("Has lowercase")
        if any(c.isdigit() for c in password):
            score += 1
            feedback.append("Has digit")
        if any(c in "!@#$%^&*()-_+=[]{}|;:,.<>?/~`" for c in password):
            score += 1
            feedback.append("Has special")
        # Reuse same labels as original script
        strength = "Very Weak"
        if score >= 6:
            strength = "Very Strong"
        elif score >= 5:
            strength = "Strong"
        elif score >= 3:
            strength = "Medium"
        elif score >= 1:
            strength = "Weak"
        return f"Overall Strength: {strength} (Score: {score}/6)", feedback


def map_result(summary, feedback):
    """Map the check_password_strength outputs to the JSON shape the frontend expects."""
    # Extract label and score from summary string
    label = "Unknown"
    score_percent = 0
    try:
        # summary like: '... Strength: Very Strong (Score: 6/6)'
        if 'Strength:' in summary:
            part = summary.split('Strength:')[-1].strip()
            label = part.split('(')[0].strip()
            if 'Score:' in part:
                sc = part.split('Score:')[-1].split('/')[0].strip().strip(')')
                score = int(sc)
                score_percent = int(score / 6 * 100)
    except Exception:
        score_percent = 0

    # Friendly label mapping
    label_map = {
        'Very Weak': 'Very Weak',
        'Weak': 'Weak',
        'Medium': 'Medium',
        'Strong': 'Strong',
        'Very Strong': 'Very Strong'
    }

    return {
        'score': score_percent,
        'label': label_map.get(label, label),
        'feedback': feedback
    }


@app.route('/')
def index():
    # Serve the local Password.html
    return send_from_directory(HERE, 'Password.html')


@app.route('/api/check', methods=['POST'])
def api_check():
    data = request.get_json(force=True) or {}
    password = data.get('password', '')
    summary, feedback = check_password_strength(password)
    return jsonify(map_result(summary, feedback))


@app.route('/api/generate')
def api_generate():
    # Generate a reasonably strong password
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()-_+='
    pwd = ''.join(secrets.choice(alphabet) for _ in range(12))
    return jsonify({'password': pwd})


if __name__ == '__main__':
    # Run on all interfaces for easier local testing; change host if you prefer.
    print(f"Starting Password app from {HERE}\nServing Password.html and API endpoints on port 5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
