FROM php:apache

RUN apt-get update; \
	apt-get install -y \
        git \
		wget \
		unzip \
		python3.9\
		python3-pip \
		libgpiod2 \
	; \
	pip3 install Adafruit-DHT;\
	a2enmod rewrite;\
	/etc/init.d/apache2 restart;\
	docker-php-ext-install mysqli; \
	docker-php-ext-enable mysqli; \
	pip3 install mysql-connector-python;\
	rm -r /var/www/html ; \
	cd /var/www ; \
	git clone https://github.com/Acem31/capteurs_mcinfo.git /var/www/html/ ; \
	chmod 777 -R /var/www/html; \
	chmod +x /var/www/html/python/reset.py; \
	chmod +x /var/www/html/python/capteurs_temp.py; \
	chown www-data:www-data /var/www/html/ -R;

EXPOSE 80
