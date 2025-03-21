from flask import Flask , jsonify ,request
from flask_cors import CORS

from models import model , tokenizer , generate_response

app = Flask(__name__)

CORS(app)


@app.route('/generate', methods=['POST'])
def chat():
  
  
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({'error':'a prompt is required'}) , 400
    
    response = generate_response(model , tokenizer  , prompt)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)