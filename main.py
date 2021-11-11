from flask import Flask
import requests

app = Flask(_name_)

def searchID(id):
    print(id)

    req = requests.get("http://192.168.100.6:6000/searchID/{}".format(id))
    print(req.text)
    return req.text


def searchTopic(topic):
    req = requests.get("http://192.168.100.6:6000/searchTopic/{}".format(topic))  # send to catalog
    print(req.text)
    req.text


def purchase(id):
    req = requests.get("http://192.168.100.6:6000/purchase/{}".format(id))
    print(req.text)
    req.text


while (True):
    i = int(input("Please, Enter your option from 1-3 :  1: search id.   2: search topic.   3:purchase.  4:finish. :"))

    if i == 1:
        w=int(input("Enter book id: "))
        searchID(1)
    elif i == 2:
        t = input("Enter book topic: ")
        searchTopic(t)
    elif i == 3:
        s = int(input("Enter book id: "))
        purchase(s)
    elif i == 3:
        break
    else:
        print("Error option, Try again")

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=2000)