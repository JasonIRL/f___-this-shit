f___-this-shit
==============

|license|  |size|

Code repo for the website http://fuck-this-shit.club

.. |license| image:: https://img.shields.io/badge/license-YOLO-brightgreen.svg
.. |size| image:: https://img.shields.io/github/repo-size/JasonIRL/bad-flask-app.svg?style=popout

Requirements
------------

- Python 3.7+

  - Pipenv
- Git
- Heroku CLI

Usage
-----

#. Clone the repo
#. Create the environment

   - ``pipenv install``
#. Load the environment

   - ``pipenv shell``
#. Run the flask app

   - ``flask db upgrade``
   - ``flask run``
#. Enjoy!

Deployment on Heroku
--------------------

#. Make Sure you have the Heroku CLI installed

   - ``heroku --version`` should return the version number if it
     is installed
#. Create the application

   - ``heroku apps: create <name of app>``
#. Create the database

   - ``heroku addons:add heroku-postgresql:hobby-dev -a <name of app>``
#. Add the heroku remote url to your repo

   - ``git remote add heroku https://git.heroku.com/<name of app>.git``
#. Deploy

   - ``git push heroku master``
