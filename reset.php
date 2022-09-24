<!DOCTYPE html>
<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/reset.py");
	$output = shell_exec($commande);
	echo $output;
	sleep(3);
	header('Location: http://capteurs.local');
  	exit();
?>
<html dir="ltr" lang="fr">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Chargement...</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
</style><meta name="author" content="BLOT Aymeric">
<meta http-equiv="refresh" content="900">
	</head>
<body>
	<div id='chargement'>
		Mise à jour des capteurs...
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