<?php
	/*$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py");
	$output = shell_exec($commande);*/
	$output = shell_exec('/var/www/html/python/capteurs_temp.py');
	echo $output;
	echo get_current_user();
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>