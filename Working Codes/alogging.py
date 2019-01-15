# import logging
# from logging import FileHandler,WARNING
# from flask import Flask

# app = Flask(__name__)

# if not app.debug:
#     file_handler = FileHandler('error.txt')
#     file_handler.setLevel(WARNING)

#     app.logger.addHandler(file_handler)

# @app.route('/')
# def index():
#     return 1 / 0

# app.run()

import logging
from flask import Flask, jsonify
app = Flask(__name__)
# if __name__ != '__main__':
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
@app.route('/')
def default_route():
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')
    return jsonify('hello world')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# import datetime
# import time

# # import colors
# from flask import g, request, Flask
# # from rfc3339 import rfc3339

# app = Flask(__name__)


# @app.before_request
# def start_timer():
#     g.start = time.time()

# from flask import request, jsonify, Flask

# app = Flask(__name__)


# @app.route('/hello', methods=['GET'])
# def hello():
#     return "Hello World"


# @app.after_request
# def log_request(response):

#     now = time.time()
#     duration = round(now - g.start, 2)
#     dt = datetime.datetime.fromtimestamp(now)
#     # timestamp = rfc3339(dt, utc=True)

#     ip = request.headers.get('X-Forwarded-For', request.remote_addr)
#     host = request.host.split(':', 1)[0]
#     args = dict(request.args)

#     log_params = [
#         ('method', request.method, 'blue'),
#         ('path', request.path, 'blue'),
#         ('status', response.status_code, 'yellow'),
#         ('duration', duration, 'green'),
#         ('ip', ip, 'red'),
#         ('host', host, 'red'),
#         ('params', args, 'blue')
#     ]

#     request_id = request.headers.get('X-Request-ID')
#     if request_id:
#         log_params.append(('request_id', request_id, 'yellow'))

#     parts = []
#     for name, value, color in log_params:
#         part = "{}={}".format(name, value)
#         parts.append(part)
#     line = " ".join(parts)

#     app.logger.info(line)

#     return response

# if __name__ == '__main__':
#     app.run(port=5000,debug=True)