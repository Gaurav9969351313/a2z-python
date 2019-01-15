from flask import Flask
from flask_pymongo import PyMongo
from flask import request, jsonify
from io import BytesIO
import base64
import re
import json
from PIL import Image
import os

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/chatbotApiDB"
mongo = PyMongo(app)

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find_one(query)
        return jsonify(data), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('name', None) is not None and data.get('email', None) is not None:
            mongo.db.users.insert_one(data)
            return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

@app.route('/uploadImagae', methods=['post'])
def uploadImagae():
    image_data = request.form['data']
    name = request.form['name']
    if not os.path.exists(name):
        os.makedirs(name)
    for i in range(3):
        im = Image.open(BytesIO(base64.b64decode(image_data[i]+ "==")))
        im.save(name+'/'+name+'_'+ str(i) +'.png')
    return json.dumps({'result': 'success'}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run(port=5000,debug=True)

