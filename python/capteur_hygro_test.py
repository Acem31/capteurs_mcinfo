import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D25, use_pulseio=False)

while True:
    try:
        humidity = dhtDevice.humidity
        print(
            "Humidity: {}% ".format(
                humidity
            )
        )

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
