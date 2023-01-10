from mqtt import mqtt

client=mqtt.connect_mqtt()
mqtt.publish(client=client,topic1="iiot/test",msg=1)