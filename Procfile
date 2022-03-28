web: gunicorn meeting_website.wsgi  --chdir ~/meeting_website --log-file - --log-level debug
python manage.py collectstatic --chdir ~/meeting_website
heroku ps:scale web=1
