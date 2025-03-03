import os

from flask import Flask, request, jsonify,render_template
from pymongo import MongoClient
from datetime import datetime
app = Flask(__name__)

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client[os.getenv("MONGO_CLUSTER")]
collection = db[os.getenv("MONGO_COLLECTION")]

counter = 0
limit = 100

latest_data = {
    "temperature": None,
    "humidity": None
}

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/render_endpoint', methods=['POST'])
def receive_data():
    global latest_data,counter
    data = request.get_json()
    if data:
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        latest_data = {
            "temperature": temperature,
            "humidity": humidity,
            "created_at": datetime.utcnow()
        }

        counter+=1
        if counter>=limit:
            temperature_data = {"type": "temperature", "value": temperature}
            humidity_data = {"type": "humidity", "value": humidity}

            collection.insert_one(temperature_data)
            collection.insert_one(humidity_data)

            counter=0

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


