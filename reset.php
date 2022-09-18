<?php
	exec("/usr/bin/python /var/www/html/python/reset.py");
	header('Location: http://capteurs.local');
  	exit();
		?>