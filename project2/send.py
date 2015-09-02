
import requests
import json
import csv

def readCSV(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        my_list = list(reader)
    return my_list

if __name__ == "__main__":
    trueFront = readCSV('2.csv')
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #addr = "http://127.0.0.1:8081/api"
    addr = "http://elb-auto-scaling-group-1055027372.ap-southeast-2.elb.amazonaws.com"
    #addr = "http://ec2-54-79-61-86.ap-southeast-2.compute.amazonaws.com"
    proxies = {
        "http": "http://tanboxi:90909900tanN@www-cache2.ecs.vuw.ac.nz:8080",
            }
    igd_list = []
    for j in range(1, 50):
        igd = 0
        count = 0
        for i in range(1, 40):
            frontName = "/home/st-james1/tanboxi/588_project/code/MOPSOCD/logData/12/" + str(i) + "/" + str(j) + "/front.csv"
            front = readCSV(frontName)
            data = {'trueFront':trueFront, 'front':front}
            req = requests.post(addr, data = json.dumps(data), headers = headers, proxies = proxies)
            print(req)
            try:
                print "received data: ", json.loads(req.text)
                igd = igd + float(json.loads(req.text))
                count = count + 1
            except:
                pass
        igd_list.append(igd/count)

    print igd_list
