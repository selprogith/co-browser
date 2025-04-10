
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "MCP Browser attivo e pronto a navigare!"

@app.route("/navigate", methods=["POST"])
def navigate():
    data = request.json
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "URL mancante"}), 400

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Estrai solo il testo leggibile (senza HTML)
        text = soup.get_text(separator=' ', strip=True)

        # Restituisci solo i primi 1000 caratteri per non appesantire
        return jsonify({
            "url": url,
            "content": text[:1000] + ("..." if len(text) > 1000 else "")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
