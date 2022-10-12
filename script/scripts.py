import subprocess
import os

cmd1 = 'docker exec -ti appache_www chown root.gpio /dev/gpiomem'
cmd2 = 'docker exec -ti appache_www chmod g+rw /dev/gpiomem'
cmd3 = 'docker exec -ti appache_www chown root.gpio /sys'
cmd4 = 'docker exec -ti appache_www chmod g+rw /sys'

os.system(cmd1)
os.system(cmd2)