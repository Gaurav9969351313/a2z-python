from flask import Flask,Response,jsonify,request
import json

app = Flask(__name__)
print(__name__)

employess = [{"firstName":"Gaurav","lastName":"Talele","age":25},
             {"firstName":"Kajal","lastName":"Talele","age":21},
             {"firstName":"Rekha","lastName":"Talele","age":45},
             {"firstName":"Yashrekha","lastName":"Talele","age":50}
            ]

@app.route('/')
def hello_world():
    return "Hello World"

# GET --> /employees 
@app.route('/employees')
def getAllBooks():
    return jsonify({ "employees" : employess })    

# POST --> /employees/25
@app.route('/employees/<int:age>', methods=['GET'])
def getEmployeesByAge(age):
    ret_val = {}
    for employes in employess:
        if employes["age"] == age:
            ret_val = { 
                "firstName":employes["firstName"],
                "lastName":employes["lastName"]
             }
    return jsonify({"ret_val": ret_val})

@app.route('/employees', methods=['POST'])
def createEmployee():
    reqData = request.get_json()
    newEmp = {
        "firstName":reqData["firstName"],
        "lastName":reqData["lastName"],
        "age":reqData["age"]
    }
    employess.insert(0,newEmp)
    sucessResp = {
        "ResponseStatus":"true",
        "ResponseString":"Employee Created Sucessfully."
    }
    response = Response(json.dumps(sucessResp),status=201,mimetype='application/json')
    return response

@app.route('/employees/<int:age>', methods=['DELETE'])
def deleteEmpByAge(age):
     for employes in employess:
        if employes["age"] == age:
            employess.pop(0)

            sucessResp = {
                "ResponseStatus":"true",
                "ResponseString":"Employee Deleted Sucessfully."
            }

            response = Response(json.dumps(sucessResp), status=400,mimetype='application/json')
            response.headers["Location"] = "/employees/" + str(age)
            return response
        else:
            errorResp = {
                "ResponseStatus":"false",
                "ResponseString":""
            }
            response = Response(json.dumps(errorResp),status= 404,mimetype='application/json')
            response.headers["Location"] = "/employees/" + str(age)
            return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'ResponseStatus': 404,
            'messResponseString': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


app.run(port=5000)