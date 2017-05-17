
## Quick start

Only 5 steps to start project.


#### Step 1

Run the following commands to create virtual environment and install
project dependencies.

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```


#### Step 2

Create database and run migrations on it.

```bash
create DB product_db
python manage.py migrate
```


#### Step 3

Create superuser for access to admin page using following command.

```bash
python manage.py createsuperuser --settings=myshop.settings.production
```


#### Step 4

Run the command below in your terminal to start server.

```bash
python manage.py runserver --settings=myshop.settings.production
```


#### Step 5

Well done! Enjoy.


---

**Make a note**, part `--settings=myshop.settings.production` 
is the additional option that points to specific settings file, 
*production* version in this case.
