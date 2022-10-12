<!DOCTYPE html>
<html dir="ltr" lang="fr">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Archives des capteurs</title>
    <link rel="stylesheet" href="capteurs.css" media="screen">
    <link rel="stylesheet" href="print.css" media="print">
	<link rel="icon" href="favicon.ico" />
	<meta name="author" content="BLOT Aymeric">
<meta http-equiv="refresh" content="900">
  </head>
  <body>
      <div id="menu">
		  <img src="img/Logo_MC_Informatique_blue.png" alt="Logo MC Informatique" align="left">
        <ul>
			<li><a href="./archiveshum.php" title="Archives des capteurs hygrométriques" target="_self">Archives-Hygro</a></li>
          	<li><a href="./index.php" title="Valeurs en direct" target="_self">Direct</a></li>
          	<li><a href="./archives.php" title="Archives des capteurs de température" target="_self">Archives-Temp</a></li>
        </ul>
      </div>
	  <div id="main">
		<div class="zone">
        <div class="capt">
			<h2>Hygrométrie 1</h2>
			<table>
			<?php
				$mysqli = new mysqli("mysql_db", "root", "couchpass31", "couch_DB");
    			if($mysqli === false){
      				die("Problème de base de données! " . mysqli_connect_error());
  				}
				$requete = "SELECT * FROM hygro1 ORDER BY id DESC";
				$resultat = mysqli_query($mysqli, $requete);

				while ($ligne = $resultat->fetch_assoc()) {
					printf("<tr><td>%s &#37;</td><td>%s</td><td>%s</td></tr>", $ligne["humidite"], $ligne["horodatage"], $ligne["date"]);
				}
				?>
			</table>
		</div>
			<div class="capt">
				<h2>Hygrométrie 2</h2>
				<table>
			<?php
				$requete = "SELECT * FROM hygro2 ORDER BY id DESC";
				$resultat = mysqli_query($mysqli, $requete);

				while ($ligne = $resultat->fetch_assoc()) {
					printf("<tr><td>%s &#37;</td><td>%s</td><td>%s</td></tr>", $ligne["humidite"], $ligne["horodatage"], $ligne["date"]);
				}
				?>
					</table>
		</div>
		</div>
	<?php
	$mysqli->close();
	?>
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
