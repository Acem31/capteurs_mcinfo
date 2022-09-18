<?php
	$commande = escapeshellcmd ('/usr/bin/python ./python/reset.py');
	//$commande = escapeshellcmd ('/usr/bin/python -V');
	$output = shell_exec($commande);
		echo $output;
	/*header('Location: http://capteurs.local');*/
  	exit();
		?>