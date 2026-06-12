from flask import Flask, request, jsonify
import json, os, uuid

app = Flask(__name__)

latest_signal = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_signal
    data = request.json
    if not data:
        return jsonify({"status": "error"}), 400
    data['id'] = str(uuid.uuid4())[:8]
    latest_signal = data
    print(f"Signal received: {data}")
    return jsonify({"status": "ok", "signal": data}), 200

@app.route('/signal', methods=['GET'])
def get_signal():
    if not latest_signal or not latest_signal.get('action'):
        return jsonify({"action": ""}), 200
    return jsonify(latest_signal), 200

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running!", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
