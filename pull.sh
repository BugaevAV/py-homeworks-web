#!/bin/bash
cd /home/alexb/py-homeworks-web
git pull origin workflow
cd /home/alexb/py-homeworks-web/1.5-ci-cd
sudo docker-compose down -v
sudo docker-compose up -d --build
sudo docker-compose exec stock_app python manage.py collectstatic
