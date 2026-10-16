
import os
import time
import paho.mqtt.client as mqtt

HOST = os.environ["MQTT_HOST"]
PORT = int(os.getenv("MQTT_PORT", "8883"))
USERNAME = os.environ["MQTT_USERNAME"]
PASSWORD = os.environ["MQTT_PASSWORD"]

TOPIC = "ois/Nurhan/commands/led"

def on_connect(client, userdata, flags, reason_code, properties):
    print("MQTT connection result:", reason_code)
    if reason_code == 0:
        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)

def on_message(client, userdata, msg):
    print("Topic:", msg.topic)
    print("Message:", msg.payload.decode(errors="replace"))

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="github-esp32-subscriber"
)

client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()
client.on_connect = on_connect
client.on_message = on_message

try:
    print("Connecting to HiveMQ Cloud...")
    client.connect(HOST, PORT, keepalive=60)
    client.loop_start()
    time.sleep(60)
finally:
    client.loop_stop()
    client.disconnect()
    print("MQTT listener stopped.")
