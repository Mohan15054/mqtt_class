import random
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
port = os.getenv("MQTT_PORT")
keep_alive = os.getenv("MQTT_KEEPALIVE")
tls_status = str2bool(os.getenv("MQTT_TLS"))
ca_cert_path = os.getenv("MQTT_CA_CERT_PATH")
insecure_tls = os.getenv("MQTT_TLS_VERIFY_DISABLE")
ws_path = os.getenv("MQTT_WS_PATH")
client_id = os.getenv("CLIENT_ID")

print("connection_type",tls_status)

print("connection_type",connection_type)

