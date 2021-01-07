###Recruitment web application using django rest framework
In the root folder of the project ( folder containing requirements.txt and manage.py)
run:
```
pip install -r requirements.txt
```


###Open settings.py and edit the DATABASE settings to your MySql specifics
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

```
###Change the NAME, USER, PASSWORD, HOST  and PORT  as appropriate

###These values are gotten from your mysql database.


###For a fresh install run:
```
python manage.py makemigrations
```
###Then run
```
python manage.py migrate
```
###This will create the necessary tables in the database

###To create a superuser
python manage.py createsuperuser

###Then run:
```
python manage.py runserver
```