<?php
	$commande = escapeshellcmd ('python /var/www/html/python/reset.py')
	$output = shell_exec($commande)
	header('Location: http://capteurs.local');
  	exit();
		?>