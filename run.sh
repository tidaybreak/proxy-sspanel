cd /data/ofidc/docker-volume/proxy-sspanel

export MYSQL_HOST="172.18.0.5"
export MYSQL_USER="root"
export MYSQL_PASSWORD="ti999"

python manage.py runserver 0.0.0.0:9000
