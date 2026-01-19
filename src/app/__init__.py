from flask import Flask
from flask import request,jsonify
from service.messageService import MessageService



app=Flask(__name__)
app.config.from_pyfile('config.py')

messageService=MessageService()

@app.route('/v1/ds/message/',methods=['POST'])
def handle_message():
    message=request.json.get('message')
    result=messageService.process_message(message)
    if result is None:
        return jsonify({"error": "Message is not a valid bank message"}), 400
        
    # 'result' is the Pydantic Expense object from LLMService
    # In Pydantic v2, use .model_dump() instead of .dict()
    return jsonify(result.model_dump()), 200



@app.route("/",methods=['GET'])
def handle_get():
    print("Hello world")

if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=True)

