

To install psycopg2 for postgres (with virtual env), see
https://gist.github.com/geekforbrains/3a2836dac8a147a91b0600fcfff3c58d
(commande = env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2)

source desktopEnv/bin/activate.fish

python manage.py makemigrations desktopTest
python manage.py sqlmigrate desktopTest 0001
python manage.py migrate

python manage.py runserver

python3 manage.py shell

python manage.py createsuperuser
userName:admin
password:yoyolepib
email:yolan.pibrac@gmail.com