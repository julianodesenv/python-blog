# Blog in python

## Install packages
- pip install django
- pip install pillow django-summernote mysqlclient
- install mysqlclient
-- https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
-- pip install https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

## Create project and modules
- django-admin startproject blog .
- python manage.py startapp categories
- python manage.py startapp posts
- python manage.py startapp comments

## Migrations
- python manage.py makemigrations
- python manage.py migrate

## Create Super User admin
- python manage.py createsuperuser

## Run server
- python manage.py runserver

## Deploy
- Create file local_settings
- python manage.py collectstatic
