from flask import Flask,Response,jsonify,request
from flaskext.mysql import MySQL
import json

mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'javaDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

class ApiResponse:
  def __init__(obj,**kwargs):
    obj.ResponseCode = kwargs.get('ResponseCode', None)
    obj.ResponseStatus = kwargs.get('ResponseStatus', None)
    obj.ResponseString = kwargs.get('ResponseString', None)
    obj.ResponseObject = kwargs.get('ResponseObject', None)

  def createCustomResponse(obj):
    ret_val = { 
                "ResponseCode":obj.ResponseCode,
                "ResponseStatus":obj.ResponseStatus,
                "ResponseString":obj.ResponseString,
                "ResponseObject":obj.ResponseObject
              }
    return jsonify({"Response": ret_val})

@app.route('/')
def hello_world():
    return "This is chatbot api"

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    # print(data.get('username'))
    username = data["username"]
    password = data["password"]

    if data.get('username', None) is not None and data.get('password', None) is not None:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from tbl_User where Username='" + username + "' and Password='" + password + "'")
        sqlData = cursor.fetchone()

        if sqlData is None:
            resp = ApiResponse(ResponseCode=200, ResponseStatus="false",ResponseString = "POST Username or Password is wrong",ResponseObject = "")
            c = resp.createCustomResponse() 
            return c
        else:
            resp = ApiResponse(ResponseCode=200, ResponseStatus="true",ResponseString = "POST Logged in successfully",ResponseObject = "")
            c = resp.createCustomResponse() 
            return c

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from tbl_User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    
    if data is None:
        resp = ApiResponse(ResponseCode=200, ResponseStatus="false",ResponseString = "Username or Password is wrong",ResponseObject = "")
        c = resp.createCustomResponse() 
        return c
    else:
        resp = ApiResponse(ResponseCode=200, ResponseStatus="true",ResponseString = "Logged in successfully",ResponseObject = "")
        c = resp.createCustomResponse() 
        return c



app.run(port=5000)