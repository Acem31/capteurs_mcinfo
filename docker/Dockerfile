FROM php:apache

RUN apt-get update; \
	apt-get install -y \
        git \
		wget \
		unzip \
		python\
	; \
	a2enmod rewrite;\
	/etc/init.d/apache2 restart;\
	docker-php-ext-install mysqli; \
	docker-php-ext-enable mysqli; \
	rm -r /var/www/html ; \
	cd /var/www ; \
	git clone https://github.com/Acem31/capteurs_mcinfo.git /var/www/html/ ; \
	chmod 777 -R /var/www/html; \
	chown www-data:www-data /var/www/html/reset.php; \
	chmod u+x /var/www/html/python/reset.py;

EXPOSE 80