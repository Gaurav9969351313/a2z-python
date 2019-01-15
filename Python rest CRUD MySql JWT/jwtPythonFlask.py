# from flask import Flask, jsonify, request,make_response
# import jwt
# import datetime
# from functools import wraps

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'thisismykey'

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
#         print(token)

#         if not token:
#             return jsonify({'message':'Token is missing...!'}) , 403
        
#         try:
#             data = jwt.decode(token,app.config['SECRET_KEY'])
#         except:
#             return jsonify({'message':'Token is invalid...!'}) , 403
        
#         return f(*args,**kwargs)

# @app.route('/unprotected')
# def unprotected():
#     return jsonify({'message':'this is available for everyone'})

# @app.route('/protected')
# @token_required
# def protected():
#     return jsonify({'message':'this cant be accesed without token'})

# @app.route('/login')
# def login():
#     auth = request.authorization
#     print(auth)
#     # if auth and auth.password == 'password':
#     token = jwt.encode({'username':'Gaurav','exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
#     return  jsonify({'token':token.decode('UTF-8')})

#     # return make_response("could not verify...!",404,{'WWW-Authenticate': 'basic-realm="Login Requird"'})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


# POST  http://localhost:5000/auth {"username":"masnun","password":"abc123"}
# GET http://localhost:5000/api/v1/private Header Authorization : JWT { token }



from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

api = Api(app, prefix="/api/v1")

USER_DATA = {
    "masnun": "abc123"
}

class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=123)


def identity(payload):
    print(payload)
    user_id = payload['identity']
    return {"user_id": user_id}


jwt = JWT(app, verify, identity)


class PrivateResource(Resource):
    @jwt_required()
    def get(self):
        return {"meaning_of_life": 42}

@app.route('/another', methods=['POST'])
def another():
    return "Hello World."




api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, jsonify, request

# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
# )

# app = Flask(__name__)

# # IMPORTANT: Body is meaningless in GET requests, so using json
# # as the only lookup method means that the GET method will become
# # unauthorized in any protected route, as there's no body to look for.

# app.config['JWT_TOKEN_LOCATION'] = ['json']
# app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

# jwt = JWTManager(app)


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     if username != 'test' or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401

#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token)


# # The default attribute name where the JWT is looked for is `access_token`,
# # and can be changed with the JWT_JSON_KEY option.
# # Notice how the route is unreachable with GET requests.
# @app.route('/protected', methods=['GET', 'POST'])
# @jwt_required
# def protected():
#     return jsonify(foo='bar')

# if __name__ == '__main__':
#     app.run()
