# getExternalLinksDockerTraefik

if you use docker containers together with the Traffic reverse proxy server and its settings are set in container labels, then this script outputs a summary table for all containers with external links

for example, there is a docker-compose file in the project.yml for creating a test environment with containers

to run the script, copy it to disk and type:
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000

then type http://YOUR_SERVER_IP:8000 in the your browser and you will get a table as a result:

1 Container name = nginx01 / URL (one) = https://nginx01.test
2 Container name = nginx04 / URL (one) = https://nginx04.test
3 Container name = nginx02 / URL (one) = https://nginx02.test 
