#!/usr/bin/env python3

import requests
import paho.mqtt.client as mqtt
import time

# Or use: giv-project2
host_name = "10.6.4.7"
port = 1883

logger_address = "http://192.168.3.30"

## helper function to request string from logger
def logger(request):
    ### forward requests directly to the logger 
    requestURL = logger_address+"/?"+request
    #print(requestURL)
    r = requests.get(requestURL)
    ### is r.text the right way to access to logger data? 
    #print(r.text)
    ### return the returned json to the client
    return (r.text)

client = mqtt.Client()
client.connect(host_name, port)

internet_connection = True
while(internet_connection):
    ## call function 
    jsonString = logger("command=dataquery&uri=dl:Public&format=json&mode=most-recent")
    ## publish mqtt
    client.publish("messwerte", jsonString)
    ## wait one second to request new values
    time.sleep(1)
# # Loop; exit on error
rc = 0
while rc == 0:
    rc = client.loop()
    print("rc: " + str(rc))


