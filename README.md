# TaskFlow — Task Management API

TaskFlow is a lightweight REST API built with FastAPI and deployed on Oracle Cloud Infrastructure (OCI).

The project demonstrates a basic DevOps workflow covering application development, Git version control, CI automation, Linux server deployment, networking, service management, and basic monitoring.

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> Test
   |
   +--> Build / Validate
   |
   v
Oracle Cloud Infrastructure
   |
   v
Oracle Linux VM
   |
   v
systemd
   |
   v
Uvicorn
   |
   v
FastAPI Application
Tech Stack
Python
FastAPI
Uvicorn
Git & GitHub
GitHub Actions
Oracle Cloud Infrastructure (OCI)
Oracle Linux 9
systemd
Linux networking and firewall
REST API
Docker configuration
API Endpoints
Method	Endpoint	Description
GET	/	API status
GET	/health	Health check
POST	/tasks	Create a task
GET	/tasks	Retrieve all tasks
PATCH	/tasks/{task_id}	Mark a task as completed
DELETE	/tasks/{task_id}	Delete a task
Deployment

The application is deployed on an Oracle Linux 9 virtual machine running on OCI.

Deployment flow:

Internet
   |
   v
OCI Public IP
   |
   v
OCI Network Security Group
   |
   v
Linux Firewall
   |
   v
systemd
   |
   v
Uvicorn
   |
   v
FastAPI

The application runs as a systemd service so that it starts automatically when the server boots and restarts if the process fails.

CI Pipeline

GitHub Actions is used for continuous integration.

The pipeline validates the project automatically when changes are pushed to GitHub.

Current CI workflow:

Git Push
   |
   v
GitHub Actions
   |
   v
Install Dependencies
   |
   v
Validate Application
   |
   v
CI Result
Cloud Infrastructure

The OCI environment includes:

Oracle Linux 9 virtual machine
Public subnet
Virtual Cloud Network (VCN)
Network Security Group
TCP port 8000 ingress
Linux firewall configuration
OCI Compute Instance Monitoring
Troubleshooting

Several deployment issues were encountered and resolved during development.

Python dependency compatibility

The OCI server uses Python 3.9, while the initial dependency versions generated from the development environment required newer Python versions.

The requirements were adjusted to versions compatible with Python 3.9.

Linux firewall

The application was initially listening on port 8000 but could not be reached externally.

The Linux firewall was configured to allow TCP port 8000.

systemd service

The first systemd configuration produced an execution permission error.

The service was changed to launch Uvicorn through Python:

python -m uvicorn

An existing manually started Uvicorn process was also stopped so that systemd could take ownership of port 8000.

Docker

A Dockerfile is included in the repository and Docker was tested as part of the project.

However, the final OCI deployment does not use Docker.

The Always Free VM has limited resources, and attempts to install container tooling on the 1 GB Oracle Linux instance repeatedly resulted in out-of-memory failures.

Rather than treating an unstable container runtime as a working deployment, the final application was deployed directly using Python, Uvicorn, and systemd.

This limitation is documented intentionally.

Monitoring and Logging

Basic operational monitoring is provided through:

OCI Compute Instance Monitoring
systemd service status
journalctl logs
/health API endpoint
Uvicorn application logs
Limitations

Task data is currently stored in application memory.

This means data is lost when the application restarts.

The project intentionally keeps the architecture small to demonstrate the deployment and DevOps workflow without introducing unnecessary infrastructure.

The current deployment also uses HTTP rather than HTTPS.

Future Improvements

Possible future improvements include:

PostgreSQL or MySQL database
HTTPS with a domain and SSL certificate
Automated deployment through CI/CD
Containerized production deployment
Centralized logging
Monitoring alerts
Separate development, staging, and production environments
Infrastructure as Code using Terraform
Kubernetes deployment
Project Status

Deployed and operational on Oracle Cloud Infrastructure.

The API has been tested on the OCI server with complete CRUD operations:

Create ✅
Read ✅
Update ✅
Delete ✅