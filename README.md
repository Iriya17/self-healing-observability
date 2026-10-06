# Self-Healing Observability & Automated Remediation

## Overview

A containerized observability and self-healing system that automatically detects application failures, triggers alerts, and performs automated remediation without manual intervention.

The project demonstrates an end-to-end:

**Monitoring → Alerting → Automation → Remediation → Recovery**

---

## Architecture

```text
                    ┌──────────────────┐
                    │   Flask App      │
                    │    Docker        │
                    └────────┬─────────┘
                             │
                          Metrics
                             │
                             ▼
                    ┌──────────────────┐
                    │   Prometheus     │
                    │ Monitoring       │
                    └────────┬─────────┘
                             │
                      ApplicationDown
                             │
                             ▼
                    ┌──────────────────┐
                    │  Alertmanager    │
                    │ Alert Routing    │
                    └────────┬─────────┘
                             │
                           Webhook
                             │
                             ▼
                    ┌──────────────────┐
                    │ Python/Flask     │
                    │ Remediation      │
                    └────────┬─────────┘
                             │
                       Docker API
                             │
                             ▼
                    ┌──────────────────┐
                    │ Restart Failed   │
                    │ Container        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Application      │
                    │ Recovered        │
                    └──────────────────┘

                         Grafana
                    Observability UI
                    Technologies
- Docker
- Docker Compose
- Prometheus
- Grafana
- Alertmanager
- Python
- Flask
- Docker SDK for Python
- Webhooks
- PowerShell

Project Structure
self-healing-observability/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.yml
│
├── alertmanager/
│   └── alertmanager.yml
│
├── remediation/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md

How It Works
1. The Flask application runs inside a Docker container.
2. Prometheus continuously monitors the application through the /metrics endpoint.
3. If the application becomes unavailable, Prometheus detects up = 0.
4. The ApplicationDown alert is triggered after the configured threshold.
5. Alertmanager receives the alert.
6. Alertmanager sends a webhook request to the Python remediation service.
7. The remediation service uses the Docker API to restart the failed container.
8. Prometheus detects that the application is healthy again.
9. Grafana displays the application recovery.

Automated Remediation Flow
Application Failure
        ↓
Prometheus detects up = 0
        ↓
ApplicationDown Alert
        ↓
Alertmanager
        ↓
Webhook
        ↓
Python Remediation Service
        ↓
Docker API
        ↓
Restart my-app
        ↓
Prometheus verifies recovery

Key Learning
This project demonstrates practical understanding of:
- Observability
- Metrics monitoring
- Prometheus alerting
- Alertmanager
- Webhook automation
- Docker container management
- Automated incident remediation
- Self-healing infrastructure concepts
- Monitoring-driven recovery
Future Improvements
- Deploy the architecture on AWS EC2 or EKS
- Add CPU and memory alerts
- Add Slack/Email notifications
- Add Kubernetes-based remediation
- Add CI/CD using Jenkins
- Add infrastructure provisioning with Terraform
- Add application error-rate monitoring