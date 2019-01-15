import requests
import webbrowser
import urllib
import flask
from flask import Flask, render_template, request, stream_with_context, send_file,jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

url = "https://qsdev.mahindra.com/sense/app/d5b41b5c-4b4b-4d5d-870a-f750bec36e28/sheet/LewcVW/state"

#headers = {
 #   'UserDirectory': "MAHINDRA",
  #  'UserID': "11003",
   # 'cache-control': "no-cache",
    #'Postman-Token': "74ccc0ff-95bd-40f8-8b78-7846e015083e"
    #}

#response = requests.request("GET", url, headers=headers)
#print(response.url)
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open(response.url)


class ConnectQlikEngine:
    def open_doc(self, appid):
        request = {
            'method': 'OpenDoc',
            'params': [appid],
            'handle': -1,
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response

    def get_activedoc(self):
        request = {
            'method': 'GetActiveDoc',
            'params': [],
            'handle': -1,
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response

    def get_allinfos(self, qhandle):
        request = {
            'method': 'GetAllInfos',
            'params': [],
            'handle': qhandle,
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response

    def get_script(self, qhandle):
        request = {
            'method': 'GetScript',
            'params': [],
            'handle': qhandle,
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response

    def create_app(self, appname):
        request = {
            'method': 'CreateApp',
            'params': [appname],
            'handle': -1,
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response

    def get_listoffieldshandle(self, qhandle):
        '''
        Do not call this function directly.  Used to source the handle of the Fields
        :param qhandle: handle of open document
        :return: qHandle of Object Field list
        '''
        request = {
            'method': 'CreateSessionObject',
            'params': [{"qInfo": {"qId": "", "qType": "FieldList"},
                        "qFieldListDef": {"qShowSystem": True, "qShowHidden": True, "qShowSemantic": True,
                                          "qShowSrcTables": True}}],
            'handle': qhandle,
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response['result']['qReturn']['qHandle']

    def get_listoffields(self):
        request = {
            'method': 'GetLayout',
            'params': [],
            'handle': self.get_listoffieldshandle(qhandle),
            'id': self.cur_id,
            'jsonrpc': '2.0'
        }
        json_request = json.dumps(request)
        ws.send(json_request)
        sleep(1)
        return response
	
@app.route('/get_url', methods = ['GET', 'POST'])	
def get_url():
    #if request.method == 'POST':
        #body=request.get_json()
        #doc_name=body['delete']
	#if request.method == 'GET':
     url = "https://qsdev.mahindra.com/sense/app/d5b41b5c-4b4b-4d5d-870a-f750bec36e28/sheet/LewcVW/state"
    # url = "https://qsdev.mahindra.com/hub"
    headers = {
        'UserDirectory': "MAHINDRA",
        'UserID': "11003",
        'cache-control': "no-cache",    
        'Postman-Token': "74ccc0ff-95bd-40f8-8b78-7846e015083e"
    }
    response = requests.request("GET", url, headers=headers)
    print(response)
    #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open(response.url)
    # qes = ConnectQlikEngine()
    # qes.open_doc("d5b41b5c-4b4b-4d5d-870a-f750bec36e28")
    # a = qes.get_activedoc()
    # print(a)
    # qhandle = a['result']['qReturn']['qHandle']
    # print(qes.get_allinfos(qhandle))
    return response.url

# @app.route('/getDashboardUrl', methods = ['GET', 'POST'])	
# def getDashboardUrl():
#     obj = new 


if __name__ == "__main__":
	app.run(debug = True,port=8000)
    
