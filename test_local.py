"""Run local tests against the Flask app without opening network sockets.

Usage: run this with the project's venv Python to verify endpoints work.
"""
from app import app

def run_tests():
    print('Using Flask test client to POST /api/check and GET /api/generate')
    with app.test_client() as client:
        resp = client.post('/api/check', json={'password': 'StrongP@ss1'})
        print('POST /api/check ->', resp.status_code)
        print(resp.get_data(as_text=True))

        resp2 = client.get('/api/generate')
        print('\nGET /api/generate ->', resp2.status_code)
        print(resp2.get_data(as_text=True))

if __name__ == '__main__':
    run_tests()
