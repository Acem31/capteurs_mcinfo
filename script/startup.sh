#!/bin/bash
apt update
apt install -y install python3-pip
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
apt -y install ecryptfs-utils
modprobe ecryptfs
pip3 install docker-compose
pip3 install mysql-connector-python
usermod -aG docker capteurs
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/docker/Dockerfile
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/docker/docker-compose.yml
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/python/capteurs_temp_test.py
wget https://raw.githubusercontent.com/Acem31/capteurs_mcinfo/main/python/capteur_hygro_test.py
docker-compose up -d
python capteurs_temp_test.py
python capteur_hygro_test.py
service ssh restart
reboot