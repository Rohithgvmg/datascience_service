from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
from src.app.service.messageService import MessageService 

app = Flask(__name__)
# app.config.from_pyfile('config.py')

messageService = MessageService()
producer = KafkaProducer(
    bootstrap_servers=['userinfo_kafka:29092'], 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/v1/ds/message/', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.process_message(message)
    if result is None:
        return jsonify({"error": "Invalid bank message"}), 400
    
    serialized_result = result.model_dump() 
    producer.send('expense_service', serialized_result)
    return jsonify(serialized_result), 200

@app.route("/", methods=['GET'])
def handle_get():
    return jsonify({"status": "DS Service is Running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9820, debug=True)