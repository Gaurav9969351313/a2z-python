from flask import Flask
from flask_pymongo import PyMongo
from flask import request, jsonify
from io import BytesIO
import base64
import re
import json
from PIL import Image
import os
import logging
from logging import FileHandler,WARNING
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_ORIGINS'] = ['http://localhost:4200']
app.config['MONGO_URI'] = "mongodb://localhost:27017/chatbotApiDB"

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

CORS(app)

mongo = PyMongo(app)

# Zero th Leval
landingPageBtns = { "headcount":"Head Count", 
                    "attrition":"Attrition", 
                    "newjoineereport":"New Joinee Report", 
                    "rehirereport":"RE Hire Report",
                    "genderdiversity":"Gender diversity", 
                    "seprationandretirement":"Separation And Retirement Report", 
                    "retirement":"Retirement", 
                    "managerwithhighestattrition":"Manager with highest attrition",
                    "milestoneworkanniverseryreport":"Milestone Work Anniversery Report", 
                    "birthdayreport":"Birthday Report", 
                    "educationalqualificationreport":"Educational Qualification Report",
                    "employeemovementreport":"Employee Movement Report", 
                    "rwsanctionsreport":"RW Sanctions Report", 
                    "employeeconfirmationreport":"Employee Confirmation Report",
                    "performancemanagementreport":"Performance Management Report", 
                    "rewardsandrecognitionreport":"Rewards And Recognition Report", 
                    "regrettableattrition":"Regrettable Attrition" }

# First Level
firstSetBtns = ["Permanent", "Probationer", "Trainee", "Contract", "Others", "All"]

# Second Level
secondSetBtns = ["Sector", "Business Unit", "Division", "Sub Division", "Department", "Sub Department", "Business Function", "Location"]

# Third Level
thirdSetBtns = ["Gender", "Tenure", "Age", "Band"]

btnsByIndent = {
                    "headcount":{"btns": firstSetBtns }, 
                    "attrition":{"btns": firstSetBtns },
                    "newjoineereport":{"btns": firstSetBtns },
                    "rehirereport":{"btns": firstSetBtns },
                    "genderdiversity":{"btns": firstSetBtns },
                    "seprationandretirement":{"btns": firstSetBtns },
                    "retirement":{"btns": firstSetBtns },
                    "managerwithhighestattrition":{"btns": firstSetBtns },
                    "milestoneworkanniverseryreport":{"btns": firstSetBtns },
                    "birthdayreport":{"btns": firstSetBtns },
                    "educationalqualificationreport":{"btns": firstSetBtns },
                    "employeemovementreport":{"btns": firstSetBtns },
                    "rwsanctionsreport":{"btns": firstSetBtns },
                    "employeeconfirmationreport":{"btns": firstSetBtns },
                    "performancemanagementreport":{"btns": firstSetBtns },
                    "rewardsandrecognitionreport":{"btns": firstSetBtns },
                    "regrettableattrition":{"btns": firstSetBtns },

                    "permanent":{"btns":secondSetBtns},
                    "probationer":{"btns":secondSetBtns},
                    "trainee":{"btns":secondSetBtns},
                    "contract":{"btns":secondSetBtns},
                    "others":{"btns":secondSetBtns},
                    "all":{"btns":secondSetBtns},

                    "sector":{"btns":thirdSetBtns}, 
                    "businessunit":{"btns":thirdSetBtns},
                    "division":{"btns":thirdSetBtns}, 
                    "subdivision":{"btns":thirdSetBtns}, 
                    "department":{"btns":thirdSetBtns}, 
                    "subdepartment":{"btns":thirdSetBtns}, 
                    "businessfunction":{"btns":thirdSetBtns}, 
                    "location":{"btns":thirdSetBtns}
                }

# please check
@app.route('/getUserDialogs', methods=['GET'])
def getUserDialogs():
        data = mongo.db.userDialog.find({})
        # return dumps(data)
        if data is None:
            ret_val = { 
                    "ResponseCode":200,
                    "ResponseStatus":"false",
                    "ResponseString":"",
                    "ResponseObject":{}
                }
            return jsonify({"Response": ret_val})

        else:
            ret_val = { 
                    "ResponseCode":200,
                    "ResponseStatus":"true",
                    "ResponseString":"",
                    "ResponseObject": dumps(data)
                }
            return jsonify({"Response": ret_val})


@app.route('/getBasicConfiguration', methods=['GET'])
# @cross_origin(origins="http://localhost:4200")
def getBasicConfiguration():
    basicConfDict = { }
    basicConfDict["appid"] = "85675be8-4982-487d-9d2a-ccf0c01166de"
    basicConfDict["appname"] = "MHR_BOT"
    basicConfDict["dashboardurl"] = "https://qliksenseprod1.mahindra.com/sense/app/" 
    # 85675be8-4982-487d-9d2a-ccf0c01166de/sheet/jhMqMqq/state/analysis
    
    ret_val = { 
                "ResponseCode":200,
                "ResponseStatus":"true",
                "ResponseString":"Returns App Specific Basic Configurations",
                "ResponseObject":basicConfDict
              }
    app.logger.info('/getBasicConfiguration WORKING FINE')
    return jsonify({"Response": ret_val})


@app.route('/createUser', methods=['POST'])
def createUser():
    data = request.get_json()
    if data.get('username', None) is not None and data.get('password', None) is not None:
        mongo.db.users.insert_one(data)
        ret_val = { 
                "ResponseCode":200,
                "ResponseStatus":"true",
                "ResponseString":"User Created Sucessfully",
                "ResponseObject":{}
              }
        return jsonify({"Response": ret_val})
    else:
        ret_val = { 
                "ResponseCode":200,
                "ResponseStatus":"false",
                "ResponseString":"Unable To Create User,Bad Request",
                "ResponseObject":{}
              }
        return jsonify({"Response": ret_val})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if data.get('username', None) is not None and data.get('password', None) is not None:
        data = mongo.db.users.findone(data)
        if data is not None:
            ret_val = { 
                    "ResponseCode":200,
                    "ResponseStatus":"true",
                    "ResponseString":"User Logged In Sucessfully.",
                    "ResponseObject":{"value":1}
                }
            return jsonify({"Response": ret_val})
        else:
            ret_val = { 
                    "ResponseCode":200,
                    "ResponseStatus":"true",
                    "ResponseString":"UserId and Password Is Wrong",
                    "ResponseObject":{"value":0}
                }
            return jsonify({"Response": ret_val})

@app.route('/getLandingPageLinks', methods=['GET'])
def getLandingPageLinks():
    return jsonify(landingPageBtns)


@app.route('/getButtonsByIndent/<string:indentFromUser>', methods=['GET'])
def getButtonsByIndent(indentFromUser):
   # print(btnsByIndent[indentFromUser])
   return jsonify(btnsByIndent[indentFromUser])

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

