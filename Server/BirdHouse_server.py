from flask import Flask, escape, request, render_template
from flask import jsonify
from flask_cors import CORS
import json
import time
import os
import json
import math
import numpy.ma as ma


app = Flask(__name__)
CORS(app)
# @app.route('/')
# def hello():
#     app.run(host= '0.0.0.0')
#     return render_template('index1.html')



@app.route('/post', methods = ["POST"])
def post():
    data = request.get_json()
    print(data['data'])
    with open('crossing.json','w') as f: 
        json.dump(data['data'],f)
    return ''

@app.route('/get', methods = ["GET"])
def getdata():
    BirdsCrossing = getValueFromESP()
    return jsonify({'data':BirdsCrossing})



def getValueFromESP():
    with open('crossing.json','r') as json_file:
        dataBirds = json.load(json_file)
        Birdpassed = dataBirds[0]
    return Birdpassed




app.run(host='0.0.0.0', port= 5000)


