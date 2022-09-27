<!DOCTYPE html>
<html dir="ltr" lang="fr">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Chargement...</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
	</head>
<body>
	<div id='chargement'>
	<center><div class="loader"></div></center>
	<p>Mise à jour des capteurs...</p>
	</div>
	<footer>
		<script>
        var timer = setTimeout(function() {
            window.location='./index.php'
        }, 3000);
    </script>
	  </footer>
</body>
<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/reset.py");
	$output = shell_exec($commande);
	echo $output;
  	exit();
	?>
</html>