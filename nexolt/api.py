from flask import Flask , jsonify ,request
from flask_cors import CORS
import ollama


app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
  
  
    data = request.json
    prompt = data.get("prompt", "")
    
    response = ollama.chat(model="nexolt-1", messages=[{"role": "user", "content": prompt}])
    
    return jsonify({"response": response['message']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)