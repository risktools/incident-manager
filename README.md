Incident Manager
----------------
A set of python scripts that let you import, store, search and report incidents. Incident manager is flexible, in that you can record any type of incident: IT, finance, human resource. Eventually, the goal is to build a full-fledged enterprise risk management system.

Dependencies:
------------
Python 2.7.x
Django 1.6
Database: SQLite comes with python, but you can also use any DB supported by Django including MySQL and PostgresQL


Installation:
-------------
1. Create a Django project called mysite
2. Inside that project, create an app called incidents
3. Replace mysite/incidents/models.py with the supplied file models.py
4. CD into mysite directory
5. Run python manage.py makemigrations
6. Run python manage.py migrate

You need an incident list file to import. A sample file called incidents.csv is provided.
 

The entry point is the fileimport script. Here is how to use it:

python fileimport.py -i incidents.csv -t None -p default -erasedb yes


Once imported, you can use Django, or directly access the database, to view/edit incidents.

Release History
---------------
4/16/15 alpha 0.1

Coming soon:
-----------
1. Incident search
2. Incident lifecycle management
3. Incident reporting with charts
