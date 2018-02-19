# get updates from GitHub
sudo git clone https://github.com/pnadolny13/BudgetDjangoApp

# remove everything from current deployed directory except for the db
sudo mv /home/pnadolny/firstsite/db.sqlite3 /home/pnadolny/
sudo mv /home/pnadolny/firstsite/firstsite/settings.py /home/pnadolny/
sudo rm -r /home/pnadolny/firstsite/*
sudo mv /home/pnadolny/db.sqlite3 /home/pnadolny/firstsite/

# remove the db from the git pull
sudo rm -r /home/ubuntu/BudgetDjangoApp/firstsite/db.sqlite3

# remove settings from git pull
sudo rm -r /home/ubuntu/BudgetDjangoApp/firstsite/firstsite/settings.py

# move all files to deployed directory
sudo mv /home/ubuntu/BudgetDjangoApp/firstsite/* /home/pnadolny/firstsite/
sudo mv /home/pnadolny/settings.py /home/pnadolny/firstsite/firstsite/

# update permissions
sudo chmod -R 775 /home/pnadolny/firstsite
sudo chown -R pnadolny:pnadolny /home/pnadolny/firstsite

# clean up remaining git pull files
sudo rm -r /home/ubuntu/BudgetDjangoApp


# activate virtual env
alias activate=". /home/pnadolny/Env/firstsite/bin/activate"
activate

# refresh static files
echo 'yes' | /home/pnadolny/firstsite/manage.py collectstatic

# restart uwsgi
echo 'pnadolny' | sudo systemctl restart uwsgi

exit
