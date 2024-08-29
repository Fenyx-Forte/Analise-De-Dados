#!/bin/bash

# nginx
mkdir -p /var/log/nginx
touch ./var/log/nginx/error.log
touch ./var/log/nginx/access.log

# dash_app
touch ./var/log/nginx/dash_app.access.log
touch ./var/log/nginx/dash_app.error.log

chown -R www-data:www-data /var/log/nginx

# gunicorn
mkdir -p /var/log/gunicorn
mkdir -p /var/run/gunicorn
touch ./var/run/gunicorn/gunicorn_prod.pid
touch ./var/log/gunicorn/access.log
touch ./var/log/gunicorn/error.log

chown -R www-data:www-data /var/run/gunicorn
chown -R www-data:www-data /var/log/gunicorn

# Iniciar o nginx
/usr/sbin/nginx -g 'daemon off;' &

cd src/

# Iniciar o Gunicorn
gunicorn -c ../gunicorn_prod.py
