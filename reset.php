<?php
	//$commande = escapeshellcmd ('/usr/bin/python ./python/reset.py');
	$commande = escapeshellcmd ('python ./python/capteurs_temp_test.py');
	$output = shell_exec($commande);
		echo $output;
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>