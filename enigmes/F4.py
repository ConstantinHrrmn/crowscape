from constants import Adafruit_DHT,temp,temp_sensor_type

def Start(var):
    humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)
    #print("Calibration du module")
    while humidity > 95:
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)
    #print("Calibration du module terminée")
    while humidity < 95:
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)
        
    #print("Humidité au dessus de 95")
    print("ENIGME TERMINEE %s" %Title())
    
def Enigme():
    return "Quand la boite bleu est froide, il faut la réchauffer"

def Title():
    return "Il fait froid"
