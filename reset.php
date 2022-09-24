<?php
	/*$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/reset.py");
	$output = shell_exec($commande);*/
	$output = shell_exec('/var/www/html/python/reset.py');
	echo $output;
	if(function_exists('shell_exec')) {
    echo "exec is enabled";
	}
	else header('Location: http://capteurs.local');
  	exit();
		?>