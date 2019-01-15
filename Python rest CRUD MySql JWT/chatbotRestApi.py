from flask import Flask, request, jsonify
import json
import logging
from logging import FileHandler,WARNING
from bson.json_util import dumps
from flask_cors import CORS
import constants

app = Flask(__name__)
app.config['CORS_ORIGINS'] = [constants.corsAllowedUrl]

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

app.config['MONGO_URI'] = constants.mongoDBURL

CORS(app)

# WORKING FINE
@app.route('/getBasicConfiguration', methods=['GET'])
def getBasicConfiguration():
    basicConfDict = { }
    basicConfDict["appid"] = "85675be8-4982-487d-9d2a-ccf0c01166de"
    basicConfDict["appname"] = "MHR_BOT"
    basicConfDict["dashboardurl"] = "https://qliksenseprod1.mahindra.com/sense/app/" 
    
    ret_val = { 
                "ResponseCode":200,
                "ResponseStatus":"true",
                "ResponseString":"Returns App Specific Basic Configurations",
                "ResponseObject":basicConfDict
              }
    # app.logger.info('----------/getBasicConfiguration WORKING FINE----------')
    return jsonify({"Response": ret_val})

# WORKING FINE
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        username = data["username"]
        password = data["password"]

        if data.get('username', None) is not None and data.get('password', None) is not None:
            # core logic for login
            if data is not None and (username=="Admin" and password=="Admin"):
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
                        "ResponseString":"Username Or Password Is Wrong",
                        "ResponseObject":{"value":0}
                    }
                return jsonify({"Response": ret_val})
        else:
            ret_val = { 
                    "ResponseCode":404,
                    "ResponseStatus":"false",
                    "ResponseString":"Bad Request",
                    "ResponseObject":{"value":0}
                }
            return jsonify({"Response": ret_val})
    except:
        app.logger.error('---------- /login EXCEPTION HITS ----------')
    
# WORKING FINE
@app.route('/getLandingPageLinks', methods=['GET'])
def getLandingPageLinks():
    return jsonify(constants.landingPageLinks)

# WORKING FINE
@app.route('/getButtonsByIndent/<string:indentFromUser>', methods=['GET'])
def getButtonsByIndent(indentFromUser):
    try:
        return jsonify(constants.btnsByIndent[indentFromUser])
    except:
        app.logger.error('---------- /getButtonsByIndent EXCEPTION HITS ----------')
   
if __name__ == '__main__':
    app.run(port=5000,debug=True)

