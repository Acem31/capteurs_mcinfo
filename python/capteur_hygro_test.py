import sys
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 25)

if humidity is not None:
    print("Humidity=", humidity,"%")
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)