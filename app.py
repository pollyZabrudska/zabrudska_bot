from flask import Flask, request, jsonify
import random

app = Flask(__name__)

CARDS = [
    "https://i.pinimg.com/736x/7b/9e/31/7b9e316bf56064af8c2eed276c4393c1.jpg",
    "https://i.pinimg.com/736x/3a/8a/41/3a8a41f5137ebd638b2afdca01dee798.jpg",
    "https://i.pinimg.com/736x/59/68/9f/59689fa2512a24c10ca669a7d9c6b734.jpg",
    "https://i.pinimg.com/736x/b4/0c/c1/b40cc1bbed8b6c598bcd0b229cd868f0.jpg",
    "https://i.pinimg.com/736x/93/e1/2b/93e12b809bace1bb1dc8af27fabf25cd.jpg",
    "https://i.pinimg.com/736x/60/34/28/6034280318fd48e4e192b7c30cb56072.jpg",
    "https://i.pinimg.com/736x/f6/9d/a2/f69da2f364205a442f02fc1724b057ae.jpg",
    "https://i.pinimg.com/736x/9b/ee/a4/9beea4daac3c23dc38e5845a42b7faee.jpg",
    "https://i.pinimg.com/736x/d7/7d/4c/d77d4c2778a90df1d9b58cda18d794b8.jpg",
    "https://i.pinimg.com/736x/56/b1/72/56b172cc63d0768ec5f508839c181c32.jpg",
    "https://i.pinimg.com/736x/5b/99/80/5b99801edbcaf9d46d523ef505693bdd.jpg",
    "https://i.pinimg.com/736x/ff/98/f5/ff98f551431389a48d6b82218ec91954.jpg",
    "https://i.pinimg.com/736x/ce/0f/ae/ce0faea07295f88a14af236e8688a3d8.jpg",
    "https://i.pinimg.com/736x/ef/2f/a3/ef2fa3b0a99c3cb639ac3380c316446d.jpg",
    "https://i.pinimg.com/736x/12/c8/5b/12c85b9c41cd846aae7e462784b100d2.jpg",
    "https://i.pinimg.com/736x/58/7b/9a/587b9ae5b86ef4c22a8fd23959f601dd.jpg",
    "https://i.pinimg.com/736x/98/89/33/988933fde39d1a5b4a30b5a74d52dd68.jpg",
    "https://i.pinimg.com/736x/65/4f/0d/654f0d422243030db9537f3867519041.jpg",
    "https://i.pinimg.com/736x/51/80/7d/51807d0c683be326641792e4eda7affa.jpg",
]

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    
    random_card = random.choice(CARDS)

    response = {
        "fulfillmentMessages": [
            {
                "platform": "TELEGRAM",
                "image": {
                    "imageUri": random_card
                }
            },
        ]
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
