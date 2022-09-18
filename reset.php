<?php
	//$commande = escapeshellcmd ('/usr/bin/python ./python/reset.py');
	$commande = escapeshellcmd ('ls');
	$output = shell_exec($commande);
		echo $output;
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>