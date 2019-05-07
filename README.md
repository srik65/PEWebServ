# PEWebServ
Sample Python Web Service

Prerequisites:

Docker  >= 18.09 
Docker Compose >= 1.23


Steps to start application, nginx, Kibana and Monitoring Dashboards..

git clone <repo> <br></br>
cd docker-app <br></br>
docker-compose up -d <br></br>

If docker compose completed sucessfully, you will see below containers are running.,
<br></br>
Creating prometheus                 ... done <br></br>
Creating cadvisor                   ... done <br></br>
Creating nodeexporter               ... done <br></br>
Creating grafana                    ... done <br></br>
Creating flask                      ... done <br></br>
Creating alertmanager               ... done <br></br>
Creating pushgateway                ... done <br></br>
Creating docker-app_elasticsearch_1 ... done <br></br>
Creating caddy                      ... done <br></br>
Creating nginx                      ... done <br></br>
Creating docker-app_kibana_1        ... done <br></br>
Creating docker-app_logstash_1      ... done <br></br>
Joker-2:docker-app sri$ 

<br></br>
Application URL's
<br></br>
GET -> http://localhost/persons <br></br>
POST -> http://localhost/persons <jsondata> <br></br>
<br></br>
Sample format for json data:
<br></br>
{
    "first_name": "sri",
    "surname": "yach",
    "age": "28",
    "favourite_color": black",
    "nationality": "Indian"
}
<br></br>
POST -> http://localhost/persons/<id>/delete<br></br>
GET -> http://localhost/persons/<id> <br></br>

<br></br>
Kibana URL : http://<host-ip>:5601/kibana <br></br>
<br></br>
Grafana (visualize metrics) http://<host-ip>:3000
<br></br>
Prometheus (metrics database) http://<host-ip>:9090 <br></br>
