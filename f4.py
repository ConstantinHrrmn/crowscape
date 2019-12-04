from constants import Adafruit_DHT,temp,temp_sensor_type

msg = "Quand le thé est chaud, il faut souffler sur la boite bleue."

def main():
    print(msg)
    humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)
    while humidity < 80:
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)
