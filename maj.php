<?php
	/*$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py");
	$output = shell_exec($commande);*/
	$output = shell_exec('/var/www/html/python/capteurs_temp.py');
	echo $output;
	$info = shell_exec('echo $USER');
	echo $info;
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>