
from flask import Flask, url_for, request, Response, jsonify, json, make_response
import requests
from time import gmtime, strftime, sleep
import json as js




app = Flask(__name__)


@app.route('/api', methods = ['GET', 'POST'])
def hello():
	if request.method == 'GET':
		print "Hello"
		#print readLog()
	elif request.method == 'POST':
		data = request.json
		igd = evaluate(data)
		resp = make_response(json.dumps(igd), 202)
		return resp

def evaluate(data):
    front = data['front']
    trueFront = data['trueFront']
    igd = []
    for row in trueFront:
        igd.append(minimumEdistance(row, front))
    return igd

def minimumEdistance(row, front):
    result = []
    for instances in front:
        result = distance(row, instances)
    return min(result)

def distance(row, instances):
    return (row[0] - instances[0])^2 + (row[1] - instances[1])^2

@app.route('/index.html')
def healthCheck():
    resp = make_response('', 200)
    return resp
#def log(data):
	#with open('log.json', 'w') as outfile:
		#js.dump(data, outfile)

#def send(data):
	#msg = pack(data)
	#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	#while data["order"]:
		#for i in range(3):
			#addr = 'http://' + data["order"].pop(0) + ":80/api"
			#try:
				#print "Start trying..."
				#req = requests.post(addr, data = json.dumps(msg), headers = headers, timeout = 2)
				#if req.status_code == 202:
					#print "Send Successfully"
					#return
			#except Exception, e:
				#print e
	#print "failed"
	#return

#@app.route('/log')
#def returnLog():
	#data = readLog()
	#return js.dumps(data)

#def pack(data):
	#num = 1
	#num += int(data['count'])
	#data['count'] = num
	#myvalue = "blasomething"
	#myJson = {
            #"input": data['value'],
            #"output": data['value'] + myvalue,
            #"time": strftime("%a, %d, %b %Y %H:%M:%S GMT", gmtime()),
            #"index": len(data['audit'])
            #}
	#data['value'] += myvalue
	#data['audit']["max"] = myJson
	#return data



if __name__ == "__main__":
    import os
    try:
        PORT = int(os.environ.get('SERVER_HOST', 80))
    except ValueError:
        PORT = 80
    app.run("172.31.9.21", PORT)
