Connecting Flask and Gunicorn to Nginx with docker-compose
==========================================================

Quick tutorial on how to serve requests to Flask through Gunicorn Termux Android.




Setup
=====

- Install Termux,Python,git 
- git clone 
- allow  termux allow access to phone 
-


Usage
=====

```
gunicorn --bind 0.0.0.0:8000 --workers 4 "app.create_app:create_app()"
```
