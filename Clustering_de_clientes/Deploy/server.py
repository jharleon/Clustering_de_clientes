import pandas as pd
from flask import Flask, jsonify, request
from model import Model
from logging import log

model = Model() 

# app
app = Flask(__name__)

# rotas
@app.route('/', methods=['POST'])

def predict():
    try: 
        
       
        data = request.get_json(force=True)
        result = model.predict(data) 
        return jsonify(result) 

    except Exception as e:
        log(e) 
        
        
    
if __name__ == '__main__':
    app.run(port = 5000, debug=True)


