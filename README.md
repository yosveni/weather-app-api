# weather-app-api
Weather-App-Api is a service that collects data from an Open Weather API and store it as a JSON data
# Requirements
python>=3 <br/>
Django==3.1.4<br/>
djangorestframework>=3.12.2<br/>
aiohttp>=3.7.3 <br/>
postgreSQL=12.4 <br/>
Docker
# Installation without Docker
1- Clone the project from:
 https://github.com/yosveni/weather-app-api.git <br/>
2- cd project_folder<br/>
3- Run the command: `pip3 install -r requirements.txt` <br/>
4- Create a database  <br/>
5- Set database settings (api_weather/settings.py) <br/>
 ```DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
6- Create the migrations: `python3 manage.py migrate` <br/>
7- Create a user: `python3 manage.py createsuperuser` <br/>
8- Run the project: `python3 manage.py runserver` <br/>
9- Ready. 
# Installation with Docker
1- Clone the project from:
 https://github.com/yosveni/weather-app-api.git <br/>
3- Create a database  <br/>
4- Set database settings (api_weather/settings.py) <br/>
 ```DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```
5- `docker-compose build` <br/>
6- `docker-compose run web python manage.py migrate`<br/>
7- `docker-compose run web python manage.py createsuperuser`<br/>
8- `docker-compose up`<br/>
9- Ready!!
