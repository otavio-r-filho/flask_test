# Basic API using flask

Basi flask API for testing purposes

## Flask basics

To run the application we may user the commends

**Linux**

During development set environment variable FLASK_APP
to development. In production is recomended to use other
WSGI application like Waitress, Gunicorn or uWSGI.

```
$ export FLASK_ENV=development
$ export FLASK_APP=simple_app
$ flask run -h <host ip> -p <port>
```
Alternatively we can use python
```
$ python -m flask run -h <host ip> -p <port>
```

**Windows cmd**

```
C:\path\to\app>set FLASK_ENV=development
C:\path\to\app>set FLASK_APP=main.py
C:\path\to\app>flask run -h <host ip> -p <port>
```
Or use python the same way as in Linux

```
C:\path\to\app>python -m flask run -h <host ip> -p <port>
```
