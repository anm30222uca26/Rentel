from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows the frontend to talk to the backend

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "status": "success",
        "message": "Hello from the Python backend!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
