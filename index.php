<!DOCTYPE html>
<html dir="ltr" lang="fr">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Tableau de bord des capteurs</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
</style><meta name="author" content="BLOT Aymeric">
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
          <h2>Capteur 1</h2>
			<p>	<?php
		$mysqli = new mysqli("mysql_db", "root", "couchpass31", "couch_DB");
    if($mysqli === false){
      die("Problème de base de données! " . mysqli_connect_error());
  }
		$requete = "SELECT * FROM capteur1 ORDER BY id DESC";
    $resultat = mysqli_query($mysqli, $requete);

    mysqli_data_seek($resultat, 0);
    $ligne = mysqli_fetch_row($resultat);
    printf("%s" , $ligne[1]);
    
		/*$mysqli->close();*/
		?>°</p>
        </div>
        <div class="capt">
          <h2>Capteur 2</h2>
			<p><?php
				$requete = "SELECT * FROM capteur2 ORDER BY id DESC";
    $resultat = mysqli_query($mysqli, $requete);

    mysqli_data_seek($resultat, 0);
    $ligne = mysqli_fetch_row($resultat);
    printf("%s" , $ligne[1]);
    
		/*$mysqli->close();*/
		?>°</p>
        </div>
        <div class="capt">
          <h2>Capteur 3</h2>
			<p><?php
				$requete = "SELECT * FROM capteur3 ORDER BY id DESC";
    $resultat = mysqli_query($mysqli, $requete);

    mysqli_data_seek($resultat, 0);
    $ligne = mysqli_fetch_row($resultat);
    printf("%s" , $ligne[1]);
    
		/*$mysqli->close();*/
		?>°</p>
        </div>
      </div>
      <div class="zone">
        <div id="hygro">
          <h2>Hygrométrie 1</h2>
			<p><?php
				$requete = "SELECT * FROM hygro1 ORDER BY id DESC";
    $resultat = mysqli_query($mysqli, $requete);

    mysqli_data_seek($resultat, 0);
    $ligne = mysqli_fetch_row($resultat);
    printf("%s &#37;" , $ligne[1]);
    
		/*$mysqli->close();*/
		?></p>
        </div>
		  <div id="hygro">
          <h2>Hygrométrie 2</h2>
			<p><?php
				$requete = "SELECT * FROM hygro1 ORDER BY id DESC";
    $resultat = mysqli_query($mysqli, $requete);

    mysqli_data_seek($resultat, 0);
    $ligne = mysqli_fetch_row($resultat);
    printf("%s &#37;" , $ligne[1]);
    
		/*$mysqli->close();*/
		?></p>
        </div>
		<div id="donnees">
        	<div id="reset">
          		<h2>Reset données</h2>
				<a href="./reset.php" title="Reset" target="_self">Reset</a>
        	</div>
        	<div id="refresh">
				<h2>Mise à jour</h2>
				<a href="./maj.php" title="Mise à jour" target="_self">Mise à jour</a>
			</div>
		</div>
      </div>
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
