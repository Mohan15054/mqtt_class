# python 3.8
import time
from paho.mqtt import client as mqtt_client
import os
from dotenv import load_dotenv

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

load_dotenv()
auth = os.getenv("MQTT_AUTH")
username = os.getenv("MQTT_USER")
password = os.getenv("MQTT_PASS")
connection_type = os.getenv("MQTT_CONNECTION_TYPE")
broker = os.getenv("MQTT_HOST")
port = int(os.getenv("MQTT_PORT"))
keep_alive = int(os.getenv("MQTT_KEEPALIVE"))
tls_status = str2bool(os.getenv("MQTT_TLS"))
ca_cert_path = os.getenv("MQTT_CA_CERT_PATH")
insecure_tls = str2bool(os.getenv("MQTT_TLS_VERIFY_DISABLE"))
ws_path = os.getenv("MQTT_WS_PATH")
client_id = os.getenv("CLIENT_ID")


class mqtt():
    def connect_mqtt():
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        client = mqtt_client.Client(client_id,clean_session=True, userdata=None, protocol=mqtt_client.MQTTv311,transport=connection_type)
        if connection_type == 'websockets':
            client.ws_set_options(path='/'+ws_path)
        if tls_status == True:
            if ca_cert_path != '':
                client.tls_set(ca_certs=ca_cert_path)
                client.tls_insecure_set(insecure_tls)
            else:
                client.tls_set()
                client.tls_insecure_set(insecure_tls)
        if auth == "user_pass":
            client.username_pw_set(username, password)
        client.on_connect = on_connect
        print(tls_status,"tls_status")
        client.connect(broker, port,keepalive=keep_alive)
        client.loop_start()
        return client

    def publish(client,topic1,msg):
        result = client.publish(topic1, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic1}`")
        else:
            print(f"Failed to send message to topic {topic1}")