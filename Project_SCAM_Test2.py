from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/price')
def get_price():
    url = 'https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name=Sticker%20|%20Cloud9%20(Holo)%20|%20Antwerp%202022'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
