<!DOCTYPE html>
<html dir="ltr" lang="fr">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Tableau de bord des capteurs</title>
    <link rel="stylesheet" href="capteurs.css">
	<link rel="icon" href="favicon.ico" />
</style><meta name="author" content="BLOT Aymeric">
  </head>
  <body>
    <div id="doc3" class="yui-t1">
      <div id="menu">
        <ul>
          <li><a href="./index.php" title="Valeurs en direct" target="_self">Direct</a></li>
          <li><a href="./archives.php" title="Archives des capteurs" target="_self">Archives</a></li>
        </ul>
      </div>
      <div class="zone">
        <div class="capt">
          <h2>Capteur 1</h2>
			<p>	<?php
		$mysqli = new mysqli("mysql_db", "root", "couchpass31", "couch_DB");
    if($mysqli === false){
      die("Problème de base de données! " . mysqli_connect_error());
  }
		$requete = "SELECT temperature FROM capteur1";
    $resultat = mysqli_query($mysqli, $requete);

    mysqli_data_seek($resultat, 1);
    $ligne = mysqli_fetch_row($resultat);
    printf("%s" , $ligne[0]);
    
		$mysqli->close();
		?>°</p>
        </div>
        <div class="capt">
          <h2>Capteur 2</h2>
			<p>VALEUR%?°</p>
        </div>
        <div class="capt">
          <h2>Capteur 3</h2>
			<p>VALEUR%?°</p>
        </div>
        <div class="capt">
          <h2>Capteur 4</h2>
			<p>VALEUR%?°</p>
        </div>
      </div>
      <div class="zone">
        <div id="hygro">
          <h2>Hygrométrie</h2>
			<p>VALEUR%?%</p>
        </div>
        <div id="reset">
          <h2>Reset données</h2>
			<button>Remise à zéro</button>
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
