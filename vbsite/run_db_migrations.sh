#!/bin/bash

# python manage.py runserver
python manage.py flush

python manage.py makemigrations   # edit app
python manage.py migrate --run-syncdb

python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001

python manage.py makemigrations vbcourtassign
python manage.py sqlmigrate vbcourtassign 0001

python manage.py makemigrations lets_play
python manage.py sqlmigrate lets_play 0001

python3 manage.py migrate --run-syncdb # apply changes to DB
