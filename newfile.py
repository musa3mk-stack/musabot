import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(current_dir, 'index.html')

if __name__ == '__main__':
    # Render mafi yawanci yana amfani da Port 10000 ne a tsarin Web Service
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
