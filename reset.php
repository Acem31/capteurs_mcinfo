<?php
		$mysqli = new mysqli("mysql_db", "root", "couchpass31", "couch_DB");
    if($mysqli === false){
      die("Problème de base de données! " . mysqli_connect_error());
  }
		$requete = "TRUNCATE TABLE capteur1";
    $resultat = mysqli_query($mysqli, $requete);

    
	$mysqli->close();
		?>