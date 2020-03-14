echo "---- Start initial ----"
#
cd /code/sitebase
#
echo "setup database"
python manage.py migrate
#
echo "create super user"
python manage.py createsuperuser
#
echo "---- end!! ----"
