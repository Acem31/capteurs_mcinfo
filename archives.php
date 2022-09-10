<!DOCTYPE html>
<html dir="ltr" lang="fr">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Archives des capteurs</title>
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
			<?php
				$record["18:30"] = '23.5';
				$record["18:00"] = '24';
				$record["17:30"] = '24.5';
				echo '<pre>';
				print_r($record);
				echo '</pre>';
				?>
		</div>
			<div class="capt">
			<?php
				$record["18:30"] = '23.5';
				$record["18:00"] = '24';
				$record["17:30"] = '24.5';
				echo '<pre>';
				print_r($record);
				echo '</pre>';
				?>
		</div>
			<div class="capt">
			<?php
				$record["18:30"] = '23.5';
				$record["18:00"] = '24';
				$record["17:30"] = '24.5';
				echo '<pre>';
				print_r($record);
				echo '</pre>';
				?>
		</div>
			<div class="capt">
			<?php
				$record["18:30"] = '23.5';
				$record["18:00"] = '24';
				$record["17:30"] = '24.5';
				echo '<pre>';
				print_r($record);
				echo '</pre>';
				?>
		</div>
			<div class="capt">
			<?php
				$record["18:30"] = '80%';
				$record["18:00"] = '82%';
				$record["17:30"] = '84%';
				echo '<pre>';
				print_r($record);
				echo '</pre>';
				?>
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
