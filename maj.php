<!DOCTYPE html>
<html dir="ltr" lang="fr">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Chargement...</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
</style><meta name="author" content="BLOT Aymeric">
<meta http-equiv="refresh" content="3;URL='http://capteurs.local'">
	</head>
<body>
	<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py");
	$output = shell_exec($commande);
	echo $output;
  	exit();
		?>
	<div id='chargement'>
	<div class="loader">Loading...</div>
	<p>Mise à jour des capteurs...</p>
	</div>
	<footer>
		  <center>
			  <p>Copyright 
    <?php echo date("Y"); ?> 
<a href="https://www.mc-informatique.fr/" title="Site internet de MC Informatique à l'Union (31)">mc-informatique.fr</a>. Tous droits réservés.
			  </p>
		  </center>
	  </footer>
</body>
</html>