#!/bin/bash
sleep 15
docker exec -ti appache_www chown root.gpio /dev/gpiomem
docker exec -ti appache_www chmod g+rw /dev/gpiomem