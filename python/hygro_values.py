import Adafruit_DHT

humidity1, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 6)
humidity2, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 19)

print(humidity1)
print(humidity2)