Create virtual environment (replace env for environment name)
	python -m venv env

Install Virtual Environment
	pip install virtualenv

Run environment
	djangoenv\Scripts\activate

Install Django 
	pip install django 

Start Project 
	django-admin startproject UPRM_Organizer

Start App
	python manage.py startapp (name)

Run Server
	python manage.py runserver

Stop Server
	Ctrl + C 

Create Database 
	python manage.py migrate 

Other Database Commands 
	python manage.py makemigrations 	
	python manage.py migrate --run-syncdb

	python manage.py migrate --fake APPNAME zero
	python manage.py migrate APPNAME
	python manage.py makemigrations APPNAME
	python manage.py migrate APPNAME

Create Admin Account 
	python manage.py createsuperuser

Notes: 

(domain)/admin to open administrator page 

SQLite Console 
	python manage.py dbshell

See tables 
	.tables

Quit
	.quit 

admin1
admin1pass