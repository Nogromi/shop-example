instructions for running the project

Step 1
pip install -r requirements.txt

Step 2
create DB product_db

Step 3
run the command below in your terminal
python manage.py runserver --settings=myshop.settings.production

Step 4
create Superuser for access to admin page
python manage.py createsuperuser --settings=myshop.settings.productio
...
...

Step 5
python manage.py runserver --settings=myshop.settings.production

DESCRIPTION:
--settings=myshop.settings.production  — is the additional option that points to specific  settings file  
