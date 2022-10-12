#!/bin/bash
apt update
apt install -y install docker docker-compose python3-pip libgpiod2 python-is-python3
pip3 install mysql-connector-python
pip3 install Adafruit-DHT
pip3 install mysql-connector-python
usermod -aG docker capteurs
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/docker/Dockerfile
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/docker/docker-compose.yml
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/python/capteurs_temp_test.py
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/python/capteur_hygro_test.py
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/script/droits.sh
docker-compose up -d
python capteurs_temp_test.py
python capteur_hygro_test.py
docker exec -ti appache_www chown root.gpio /dev/gpiomem
docker exec -ti appache_www chmod g+rw /dev/gpiomem
service ssh restart
reboot