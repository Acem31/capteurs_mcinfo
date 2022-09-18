<?php
	$commande = escapeshellcmd ('/usr/bin/python ./python/reset.py');
	$output = shell_exec($commande);
		echo $output;
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>