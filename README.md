# kenzie-q4-capstone

Kenzie Q4 Capstone - Red Team

BananaDog - Alpha

Description:

This is the first iteration of BananaDog, an application for a dog training business where trainers and clients can book
sessions, communicate, and access a persistent log of dogs’ info and daily reports. The app will also contain
functionality beyond scheduling and communicating, allowing trainers to automatically log times and notes for
trainings/activities per dog, per session.

This alpha version represents the first attempt to understand and manipulate Django to accomplish the goals set out for
the app. This respository will contain this version only and perhaps some updates in UI experimentation. A new version
of this project is being built (link will be added in the future) which will consider more appropriate solutions and
workflows for a produciton-level version of this app that will be used publicly and deployed.

How to run:

This version of the repository uses Poetry and Django. To spin it up from your terminal, while in the project directory,
run:

poetry install ->this will install necessary dependencies

poetry shell ->this will create the necesassary virtual environment

python manage.py createsuperuser ->follow the steps to create an admin user (access admin panel to test models/edit
database directly at http://localhost:8000/admin )

python manage.py runserver ->this will start the server at http://localhost:8000/

\*This code is shared for demonstration purposes only
