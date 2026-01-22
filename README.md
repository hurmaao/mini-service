# SRE Monitoring Stack
Full-fledged production-ready monitoring stack

## Overview

System architecture:
- **USER - (HTTP) APP [FastAPI App: 8000]**
- **APP - (Prometheus /metrics) PROM [Prometheus: 9090]**
- **PROM - (Alerts) ALERT [Alertmanager: 9093]**
- **ALERT - (Telegram) TG [Telegram Bot]**
- **PROM - (Query) GRAF [Grafana: 3000]**
- **USER - (UI) GRAF**

* API:           http://localhost:8000/health
* Prometheus:    http://localhost:9090/targets  
* Grafana:       http://localhost:3000 (admin/admin)
* Alertmanager:  http://localhost:9093/#/alerts

### API Endpoints
Endpoint         | Description                       | Response
-----------------|-----------------------------------|--------
GET /            | Health check                      | 200 OK
GET /health      | Health check + failure simulation | 200 / 503
GET /slow?ms=300 | Artificial delay                  | 200 OK
GET /error       | Error simulation                  | 500 Interval server error
GET /verion      | App version                       | 200 OK
GET /metrics     | Prometheus metrics                | 200 OK

CI/CD Pipeline 
- **PUSH - CHECKOUT)**
- **CHECKOUT - PYTHON**
- **PYTHON - INSTALL**    
- **INSTALL - BLACK**
- **BLACK - FLAKE8**
- **FLAKE8 - PYTEST**
- **PYTEST - DOCKER**
- **DOCKER - BUILDX**
- **BUILDX - META**
- **META - BUILD**
- **BUILD - SUCCESS**
