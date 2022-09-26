<!DOCTYPE html>
<html dir="ltr" lang="fr">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Chargement...</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
</style><meta name="author" content="BLOT Aymeric">
	</head>
<body>
		<div id='chargement'>
	<center><div class="loader"></div></center>
	<p>Mise à jour des capteurs...</p>
	</div>
	<footer>
		  <center>
			  <p>Copyright 
    <?php echo date("Y"); ?> 
<a href="https://www.mc-informatique.fr/" title="Site internet de MC Informatique à l'Union (31)">mc-informatique.fr</a>. Tous droits réservés.
			  </p>
		  </center>
		<script>
        var timer = setTimeout(function() {
            window.location='./index.php'
        }, 3000);
    </script>
	  </footer>
</body>
	<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/capteurs_temp.py");
	$output = shell_exec($commande);
	echo $output;
  	exit();
		?>
</html>