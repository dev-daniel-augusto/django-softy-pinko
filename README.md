<h1 align="center">Django Softy Pinko</h1>

<p align="center">A simple website built with Django and Softy Pinko HTML template</p>


![Maintained](https://img.shields.io/badge/maintained-no-FA5107?style=flat&logo=) &nbsp;
![Finished](https://img.shields.io/badge/finished-yes-00FF78?style=flat&logo=) &nbsp;
[![Python](https://img.shields.io/badge/framework-django-1B8BEF?style=flat&logo=Django)](https://www.djangoproject.com/) &nbsp;
[![Postgre](https://img.shields.io/badge/database-postgreSQL-008FFF?style=flat&logo=PostgreSQL)](https://www.postgresql.org/) &nbsp;
[![License](https://img.shields.io/badge/license-MIT-23BCC1?style=flat&logo=)](https://github.com/diz-daniel/django-softy-pinko/blob/master/LICENSE.md) &nbsp;
[![Req](https://img.shields.io/badge/requirements-here-23BCC1?style=flat&logo=)](https://github.com/diz-daniel/django-softy-pinko/blob/master/requirements.txt)

## About

This project's goal is to provide a reliable way to manipulate the informations on core page of Softy Pinko HTML directly 
from Django's Admin, so you could fill the informations in the most pleasant way for your purposes. 

## Preview

![Site](https://i.imgur.com/ZYcG6Rl.jpg)

## Features

- **Costumizable** -> Update key sections and informations of your website by using django's admin easily;
- **Additional pages** -> HTTP 404 and 500 errors pages;
- **Totally responsive website**;
- **Template inheritance** -> To help you to find sections and informations you wish modifying;
- **E-mail system** (_please, read Settings section below_);
- **API** -> This website has an API, so if you business grow up you can use your models data with another application;
- **Django JET admin** -> new admin style using the terrific [Django JET template](https://github.com/geex-arts/django-jet).
- **Tests**:

![Tests](https://i.imgur.com/bzDY2Jq.png)

## Settings

From settings.py there're some configs you'd like to do before running this project:

* **Secret Key**: the project's secret key was commit since the start of the project to provide a full overview of it.
I'd recommend changing it before running this project, specially in production.

* **Database**: this project was created using PostgreSQL database. This doesn't mean that you won't be able to use MySQL or even the default django's database (SQLite).But be aware of there's a field called _benefits_ from Pricing Model. This field is an array, which uses ArrayField from django.contrib.postgres.fields module. If you are planning to switch database you'll need adapt this field.

Basically you need to connect to your Postgre databse inside of settings.py file before making the migrations.

* **E-mails**: if you have a mail server you can just delete **_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend_**
  line from settings.py and use the righ below e-mail configs there (make sure to delete the quotation marks).
  
## How to run the project 
After setting up your database we can go ahead.

You going to need both Python and Virtualenv installed in order to run this project. In fact, Virtualenv is not required, 
but I'd recommend you having it to keep dependencies required of each project separated.

Select a directory, open you terminal and create a virtualenv with:
```
virtualenv .env
```
Now you have a virtual enviroment. The next step is active it:
```
source .env/bin/activate
```
Clone the project with: 
```
git clone https://github.com/diz-daniel/django-softy-pinko.git
```
Use the _cd_ to navigate into the project:
```
cd django-softy-pinko
```
To install the project dependencies run:
```
pip install -r requirements.txt
```
Like said before, make sure to have your database set up in settings.py before running this:
```
python manage.py makemigrations

python manage.py migrate
```
Now you can finally run the project:
```
python manage.py runserver
```
Now you can create your superuser (_python manage.py createsuperuser_) in order to log into admin. From now on you can add your own features that will be showed on index page.
