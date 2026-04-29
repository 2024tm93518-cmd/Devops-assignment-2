from flask import Flask, jsonify, request

app = Flask(__name__)
members = []

@app.route("/")
def home():
    return jsonify({"message": "ACEest Fitness & Gym Running"})

@app.route("/plans")
def plans():
    return jsonify(["Weight Loss", "Muscle Gain", "Yoga", "Cardio"])

@app.route("/member", methods=["POST"])
def add_member():
    data = request.json
    members.append(data)
    return jsonify({"status": "added", "count": len(members)})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
