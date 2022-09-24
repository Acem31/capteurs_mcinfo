<?php
include("exporter.php");
?>
<!DOCTYPE html>
<html dir="ltr" lang="fr">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Archives des capteurs</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
</style><meta name="author" content="BLOT Aymeric">
<meta http-equiv="refresh" content="1800">
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
			<h2>Capteur 1</h2>
			<table>
			<?php
				$mysqli = new mysqli("mysql_db", "root", "couchpass31", "couch_DB");
    			if($mysqli === false){
      				die("Problème de base de données! " . mysqli_connect_error());
  				}
				$requete = "SELECT * FROM capteur1 ORDER BY id DESC";
				$resultat = mysqli_query($mysqli, $requete);

				while ($ligne = $resultat->fetch_assoc()) {
					printf("<tr><td>%s°</td><td>%s</td><td>%s</td></tr>", $ligne["temperature"], $ligne["horodatage"], $ligne["date"]);
				}
			?>
			</table>
		</div>
			<div class="capt">
				<h2>Capteur 2</h2>
				<table>
			<?php
				$requete = "SELECT * FROM capteur2 ORDER BY id DESC";
				$resultat = mysqli_query($mysqli, $requete);

				while ($ligne = $resultat->fetch_assoc()) {
					printf("<tr><td>%s°</td><td>%s</td><td>%s</td></tr>", $ligne["temperature"], $ligne["horodatage"], $ligne["date"]);
				}
			?>
					</table>
		</div>
			<div class="capt">
				<h2>Capteur 3</h2>
				<table>
			<?php
				$requete = "SELECT * FROM capteur3 ORDER BY id DESC";
				$resultat = mysqli_query($mysqli, $requete);

				while ($ligne = $resultat->fetch_assoc()) {
					printf("<tr><td>%s°</td><td>%s</td><td>%s</td></tr>", $ligne["temperature"], $ligne["horodatage"], $ligne["date"]);
				}
			?>
					</table>
		</div>
			<div class="capt">
				<h2>EXporter vers Excel</h2>
				<form action="#" method="post">
				<button type="submit" id="export" name="export"
 				value="Export to excel" class="btn btn-success">Export To Excel</button>
</form>
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
