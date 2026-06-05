from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"status": "error"}), 400
    print(f"Signal received: {data}")
    with open('signal.txt', 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "ok"}), 200

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
