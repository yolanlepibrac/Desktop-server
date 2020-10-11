

# installing psycopg2 in virtualenv on macOS Sierra
https://gist.github.com/geekforbrains/3a2836dac8a147a91b0600fcfff3c58d
(commande = env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2)

# vEnv
source desktopEnv/bin/activate.fish

# Python
python manage.py runserver

python manage.py makemigrations desktopTest
python manage.py sqlmigrate desktopTest 0001
python manage.py migrate

python3 manage.py shell
python manage.py createsuperuser


# Heroku : 
heroku local
heroku config:set TIMES=2
heroku run python manage.py migrate