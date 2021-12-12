# RETO ELENAS API

## Introducción

+ [Python 3.7.6](https://www.python.org/downloads/release/python-376/).
+ Se utilizo el framework [Django](https://pypi.org/project/Django/).
+ Para las pruebas unitarias se utilizo la libreria [Unittest Django] y la aplicación Postman.    

## Prerequisitos

+ Instalar [Python 3.7.6](https://www.python.org/downloads/release/python-376/)

Habilitar entorno virtual de Python y luego instalar las dependencias del proyecto.

```commandline
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Test:
python manage.py test

Documentación:
[Documentación](http://127.0.0.1:8000/api/v1/doc/)

```

# Resumen del API Rest Elenas

Todas las peticiones a la API Rest necesitan en su encabezado un token de autorización Bearer.

```commandline
Authorization: Bearer <token>
```

## End Points

![alt text](https://github.com/jmelo77/Reto_Elenas/blob/main/endpoints.png)
