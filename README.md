# getExternalLinksDockerTraefik

if you use docker containers together with the Traefik reverse proxy server (https://traefik.io/) and its settings are set in container labels, then this script outputs a summary table for all containers with external links

for example, there is a docker-compose.yml file in the project for creating a test environment with containers

to run the script, clone repo to disk and type:
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000

then type http://YOUR_SERVER_IP:8000 in the your browser and you will get a table as a result:

1 Container name = nginx01 / URL (one) = https://nginx01.test <br/>
2 Container name = nginx04 / URL (one) = https://nginx04.test <br/>
3 Container name = nginx02 / URL (one) = https://nginx02.test 
