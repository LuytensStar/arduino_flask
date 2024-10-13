import os

from flask import Flask, request, jsonify,render_template
from pymongo import MongoClient
app = Flask(__name__)

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client['ImageCluster']
collection = db['TempCollection']

latest_data = {
    "temperature": None,
    "humidity": None
}

@app.route('/render_endpoint', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    if data:
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        latest_data = {
            "temperature": temperature,
            "humidity": humidity
        }

        temperature_data = {"type": "temperature", "value": temperature}
        humidity_data = {"type": "humidity", "value": humidity}

        collection.insert_one(temperature_data)
        collection.insert_one(humidity_data)

        print(f"Received data: Temperature={temperature}, Humidity={humidity}")
        return jsonify({"message": "Data received"}), 200
    else:
        return jsonify({"message": "No data received"}), 400

@app.route('/display', methods=['GET'])
def display_data():
    return render_template('index.html',
                           temperature=latest_data["temperature"],
                           humidity=latest_data["humidity"])

def new_func():
    pass

if __name__ == '__main__':
    app.run(debug=True)


