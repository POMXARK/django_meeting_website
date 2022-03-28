python manage.py collectstatic --chdir ~/meeting_website
python manage.py migrate --chdir ~/meeting_website
web: gunicorn meeting_website.wsgi  --chdir ~/meeting_website --log-file - --log-level debug
heroku ps:scale web=1
