
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Co-Browser MCP è attivo!"

@app.route("/navigate", methods=["POST"])
def navigate():
    data = request.json
    url = data.get("url", "")
    return jsonify({"message": f"Simulazione: navigazione verso {url} completata."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
