<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/reset.py");
	$output = shell_exec($commande);
	echo $output;
	if(function_exists('shell_exec')) {
    echo "exec is enabled";
	}
	else header('Location: http://capteurs.local');
  	exit();
		?>