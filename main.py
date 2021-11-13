import requests



def searchID(id):

    req = requests.get("http://192.168.56.102:6000/searchID/{}".format(id))
    if (req.status_code == 200):
        print (req.text)

    else:
        print('Error,status code: '+ str(req.status_code))


def searchTopic(topic):
    req = requests.get("http://192.168.56.102:6000/searchTopic/{}".format(topic))  # send to catalog
    if (req.status_code == 200):
        print(req.text)

    else:
        print('Error,status code: ' + str(req.status_code))


def purchase(id):
    req = requests.post("http://192.168.56.102:6000/purchase/{}".format(id))
    if (req.status_code == 200):
        print(req.text)

    else:
        print('Error,status code: ' + str(req.status_code))


while (True):
    i = int(input("Please, Enter your option from 1-4: \n 1: search id.\n 2: search topic. \n 3:purchase.\n 4:finish.\n"))

    if i == 1:
        w=int(input("Enter book id: "))
        searchID(w)
    elif i == 2:
        t = input("Enter book topic: ")
        searchTopic(t)
    elif i == 3:
        s = int(input("Enter book id: "))
        purchase(s)
    elif i == 4:
        exit()
    else:
        print("Error option, Try again")