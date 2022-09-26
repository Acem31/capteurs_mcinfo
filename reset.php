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
	<script type="text/javascript">
		var count = 3;
		var redirect = "./index.php";
 
		function countDown(){
    	var timer = document.getElementById("timer");
    	if(count > 0){
        	count--;
        	timer.innerHTML = "Fin de mise à jour des capteurs dans "+count+" secondes.";
        	setTimeout("countDown()", 3000);
    	}else{
        	window.location.href = redirect;
    	}
		}
</script>

	<?php
	$commande = escapeshellcmd ("/usr/bin/python3.9 /var/www/html/python/reset.py");
	$output = shell_exec($commande);
	echo $output;
  	exit();
	?>
	<div id='chargement'>
	<div class="loader">Loading...</div>
	<p>
	<script type="text/javascript">countDown();</script></p>
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