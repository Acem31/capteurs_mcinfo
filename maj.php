<?php
	$commande = escapeshellcmd ('/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py');
	$output = shell_exec($commande);
	printf($output);
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>