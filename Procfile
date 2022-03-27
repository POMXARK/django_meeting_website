web: gunicorn meeting_website.wsgi:meeting_website --log-file - --log-level debug
heroku ps:scale web=1
python manage.py migrate