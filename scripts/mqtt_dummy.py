#### pretends to send out data like the data logger
import random
import time

# pip3 install paho-mqtt
import paho.mqtt.client as mqtt


# Define variables for client 
username_id = "erictg96@googlemail.com"
password = "9157fbb4"
host_name = "mqtt.dioty.co"
port = 1883
root_topic = "/"+username_id+"/"

# Define event callbacks

def on_connect(client, userdata, rc):
    if rc == 0:
            print("Connected successfully.")
    else:
            print("Connection failed. rc= "+str(rc))

def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid "+str(mid)+" received.")

def on_message(client, userdata, msg):
    print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)

client = mqtt.Client()

# Assign event callbacks
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message

# Connect
client.username_pw_set(username_id, password)
client.connect(host_name, port)

# Start subscription
# client.subscribe("/erictg96@googlemail.com/#")

# Publish a message
for x in range(100):
    client.publish(root_topic+"des", random.randint(1,100))
    time.sleep(1)
# Loop; exit on error
rc = 0
while rc == 0:
    rc = client.loop()
    print("rc: " + str(rc))

