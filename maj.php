<?php
	/*$commande = escapeshellcmd ('/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py');*/
	$commande = escapeshellcmd ('docker exec -ti appache_www /usr/bin/python3.9 /var/www/html/python/capteurs_temp.py');
	$output = shell_exec($commande);
	echo $output;
	header('Location: http://capteurs.local');
  	exit();
		?>