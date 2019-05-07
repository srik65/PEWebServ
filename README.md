# PEWebServ
Sample Python Web Service

Prerequisites:

Docker  >= 18.09 
Docker Compose >= 1.23


Steps to start application, nginx, Kibana and Monitoring Dashboards..

git clone <repo> <br></br>
cd docker-app
docker-compose up -d 

If docker compose completed sucessfully, you will see below containers are running.,

Creating prometheus                 ... done
Creating cadvisor                   ... done
Creating nodeexporter               ... done
Creating grafana                    ... done
Creating flask                      ... done
Creating alertmanager               ... done
Creating pushgateway                ... done
Creating docker-app_elasticsearch_1 ... done
Creating caddy                      ... done
Creating nginx                      ... done
Creating docker-app_kibana_1        ... done
Creating docker-app_logstash_1      ... done
Joker-2:docker-app sri$ 


Application URL's

GET -> http://localhost/persons
POST -> http://localhost/persons <jsondata>

Sample format for json data:

{
    "first_name": "sri",
    "surname": "yach",
    "age": "28",
    "favourite_color": black",
    "nationality": "Indian"
}

POST -> http://localhost/persons/<id>/delete
GET -> http://localhost/persons/<id>


Kibana URL : http://localhost:5601/kibana

Grafana (visualize metrics) http://<host-ip>:3000

Prometheus (metrics database) http://<host-ip>:9090
