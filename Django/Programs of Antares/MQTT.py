#Install the MQTT client library with the command: pip3 install paho-mqtt

import paho.mqtt.client as mqtt
from time import sleep

# The callback function. It will be triggered when trying to connect to the MQTT broker
# client is the client instance connected this time
# userdata is users' information, usually empty. If it is needed, you can set it through user_data_set function.
# flags save the dictionary of broker response flag.
# rc is the response code.
# Generally, we only need to pay attention to whether the response code is 0.
def on_connect(client, userdata, flags, rc) : 
    if rc == 0:
        print('Connected sucess')
    else:
        print(f'Connected fail with code {rc}')
    client.subscribe('config/Raspberry') #Tail of subscription

# the callback function, it will be triggered when receiving messages
def on_message(client,userdata,msg):
    print(f"{msg.topic} {msg.payload}")

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
mqttBroker = '34.70.182.129' #Broker address
mqttPort = 1883 #Broker port number
keepAlive = 60 #Frequency Keep Alive in seconds
client.connect(mqttBroker,mqttPort,keepAlive) #Conection to broker google
# set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
client.will_set('config/keepalive/Raspberry', b'{"status": "Off"}')

for i in range(3):
    client.publish('sena/bogota/data/Raspberry','{"id":"103","v":[{"id":"DO3","v":1,"d":12651561561}]}',qos=0,retain=False)#Tail of publish
    sleep(1)

client.loop_forever() #Keep the connection forever
