#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -q -y apache2 git-core libapache2-mod-wsgi mysql-server mysql-common python3 python-imaging acl

a2enmod wsgi

usermod vagrant -a -G www-data

apt-get install -y  python-pip 

apt-get install -y libmysqlclient-dev python-dev

mysql -u root -e "create database numbas_editor;"
mysql -u root -e "grant all privileges on numbas_editor.* to 'numbas'@'localhost';"

mkdir /srv/numbas
mkdir /srv/numbas/media
mkdir /srv/numbas/previews
mkdir /srv/numbas/static

mkdir /srv/www
ln -fs /vagrant/editor /srv/www/numbas_editor
ln -fs /vagrant/numbas /srv/numbas/dist

cd /srv/numbas
chmod 2770 media previews
chmod 2750 dist static
chgrp www-data dist media previews static
setfacl -dR -m g::rwX media previews
setfacl -dR -m g::rX static

cp /vagrant/setup/database.py /srv/www/numbas_editor/numbas/database.py
cp /vagrant/setup/settings.py /srv/www/numbas_editor/numbas/settings.py
cp /vagrant/setup/django.wsgi /srv/www/numbas_editor/web/django.wsgi
cp /vagrant/setup/index.html /srv/www/numbas_editor/editor/templates/index.html

pip install -r /srv/www/numbas_editor/numbas/requirements.pip
pip install MySQL-python

cd /srv/www/numbas_editor
python manage.py syncdb --noinput
python manage.py migrate taggit
python manage.py migrate editor
python manage.py migrate accounts
python manage.py collectstatic --noinput

cp editor/templates/index.html.dist editor/templates/index.html

ln -fs /vagrant/setup/numbas_editor /etc/apache2/sites-available/numbas_editor
a2dissite default
a2ensite numbas_editor
service apache2 reload

export DJANGO_SETTINGS_MODULE=numbas.settings
export PYTHONPATH=/srv/www/numbas_editor
python /vagrant/setup/create_admin.py
