from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/scrap-astronaut")
def scrap_astronaut():
    url = "https://1win.com.ci/casino/play/100hp_100hpgaming_astronaut?castId=155477863141892096"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Remplace ceci par la bonne classe CSS selon les données que tu veux extraire
        results = soup.find_all("div", class_="multiplier")[:6]

        cotes = []
        for result in results:
            cotes.append(float(result.text.strip().replace("x", "")))

        return jsonify({
            "status": "success",
            "lastMultipliers": cotes,
            "trend": "up" if cotes[-1] > 2 else "down"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
