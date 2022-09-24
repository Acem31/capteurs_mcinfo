<?php
	/*$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py");
	$output = shell_exec($commande);*/
	$output = shell_exec('/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py');
	echo $output;
	if(function_exists('escapeshellcmd')) {
    echo "escapeshellcmd is enabled";
	}
	else header('Location: http://capteurs.local');
  	exit();
		?>