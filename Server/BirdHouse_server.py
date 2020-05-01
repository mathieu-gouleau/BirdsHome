from flask import Flask, escape, request, render_template
from flask import jsonify
from flask_cors import CORS
import json
import time
import os
import json
import math
import numpy.ma as ma


feeds = []

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
    today = date.today()
    with open('crossing.json','w') as f: 
        entry = {'date':str(today),'data':data['data']}
        feeds.append(entry)
        print("taille list")
        print(len(feeds))
        json.dump(feeds,f)
    return ''

@app.route('/get', methods = ["GET"])
def getdata():
    BirdsCrossing = getValueFromESP()
    return jsonify({'data':BirdsCrossing})



def getValueFromESP():
    with open('crossing.json','r') as json_file:
        
        dataBirds = json.load(json_file)
        print("taille list")
        print(len(feeds))
        Birdpassed = dataBirds[len(feeds)-1]["data"]
    return Birdpassed



app.run(host='0.0.0.0', port= 5000)


