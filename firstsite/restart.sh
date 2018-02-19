# refresh static files

echo 'yes' | /home/pnadolny/firstsite/manage.py collectstatic

# restart uwsgi
echo 'pnadolny' | sudo systemctl restart uwsgi

