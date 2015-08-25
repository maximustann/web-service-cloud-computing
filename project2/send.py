
import requests
import json
import csv

def readCSV(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        my_list = list(reader)
    return my_list


if __name__ == "__main__":
    data = readCSV("./2.csv")
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    addr = "http://54.206.0.192:80/api"
    #req = requests.post(addr, data = json.dumps(data), headers = headers)
    req = requests.post(addr)