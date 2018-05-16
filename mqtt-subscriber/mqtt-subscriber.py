import paho.mqtt.client as mqtt
import datetime
import time
import os

mqttServer = ""
mqttPort = 1883
mqttSubTopic = ""

# Gets the path of the python script and set a global var, "count" to keep track of number of packages received
cwd = os.getcwd()
global count
count = 1

def on_connect(mqttc, obj, flags, rc):
	print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
	global count

	with open(cwd + "/log.txt", "a+") as f:
		payload = str(count), time.ctime(), msg.topic + " " + str(msg.qos) + " " + str(msg.payload)

		print(payload)

		f.write(payload + "\n")
		f.close()

		count += 1


def on_publish(mqttc, obj, mid):
	print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
	print(time.ctime(),string)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect(mqttServer, mqttPort, 60)
mqttc.subscribe(mqttSubTopic, 0)

mqttc.loop_forever()
