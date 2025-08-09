from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return resp

@app.route('/', methods=['GET','OPTIONS'])
def health():
    return make_response(jsonify({"ok": True, "runtime": "python", "framework": "flask"}), 200)
