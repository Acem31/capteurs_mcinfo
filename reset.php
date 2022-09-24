<?php
	/*$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/reset.py");
	$output = shell_exec($commande);*/
	$output = shell_exec('/var/www/html/python/reset.py');
	echo $output;
	header('Location: http://capteurs.local');
  	exit();
		?>