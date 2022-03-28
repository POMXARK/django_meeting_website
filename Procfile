web: gunicorn meeting_website.wsgi  --chdir ~/meeting_website --log-file - --log-level debug

heroku ps:scale web=1
