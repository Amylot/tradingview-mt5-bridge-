from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    with open('signal.txt', 'w') as f:
        json.dump(data, f)
    print(f"Signal received: {data}")
    return jsonify({"status": "ok"}), 200

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running!", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
