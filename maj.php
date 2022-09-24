<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py");
	$output = shell_exec($commande);
	echo $output;
	if(function_exists('escapeshellcmd')) {
    echo "escapeshellcmd is enabled";
	}
	else header('Location: http://capteurs.local');
  	exit();
		?>