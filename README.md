# 🧰 Docker-s-Mini-Cloud - 15+ GUI Tools
It provides a self-hosted "mini cloud" environment using Docker Compose, including 15+ open-source GUI-based tools for development, monitoring, file management, and infrastructure services.

---

## 📁 Directory Structure

```
mini-cloud/
├── database/
│   ├── postgres-compose.yml
│   ├── redis-compose.yml
│   ├── mongo-compose.yml
│   ├── cassandra-compose.yml
│   └── neo4j-compose.yml
├── tools/
│   ├── portainer-compose.yml
│   ├── adminer-compose.yml
│   ├── pgadmin-compose.yml
│   ├── filebrowser-compose.yml
│   ├── appsmith-compose.yml
│   ├── nocodb-compose.yml
│   ├── code-server-compose.yml
│   ├── grafana-compose.yml
│   ├── prometheus-compose.yml
│   ├── netdata-compose.yml
│   ├── uptime-kuma-compose.yml
│   ├── vaultwarden-compose.yml
│   ├── nextcloud-compose.yml
│   └── gitea-compose.yml
├── dashboard/
│   ├── manage.py
│   ├── dashboard_project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── dashboard_app/
│       ├── templates/
│       │   └── index.html
│       ├── views.py
│       └── urls.py
├── README.md
└── requirements.txt
```

---

## 🚀 Included Tools

| Tool        | Port  | Description                           |
| ----------- | ----- | ------------------------------------- |
| Portainer   | 9000  | Manage Docker containers via GUI      |
| Adminer     | 8080  | Manage SQL databases                  |
| pgAdmin     | 5050  | PostgreSQL admin GUI                  |
| MinIO       | 9001  | S3-compatible object storage          |
| FileBrowser | 8081  | File manager with web GUI             |
| Code-Server | 8443  | VS Code in browser                    |
| NocoDB      | 8082  | Airtable-like SQL GUI                 |
| Appsmith    | 8083  | Internal tool builder                 |
| Grafana     | 3001  | Monitoring dashboards                 |
| Prometheus  | 9090  | Metrics collection                    |
| Netdata     | 19999 | Real-time system monitoring           |
| Uptime Kuma | 3002  | Website uptime monitoring             |
| Vaultwarden | 8085  | Self-hosted password manager          |
| Nextcloud   | 8086  | Cloud file storage (Google Drive alt) |
| Gitea       | 3000  | Lightweight Git server                |

---

## 🧰 Databases (Each in Separate Compose File)

* PostgreSQL (Relational)
* Redis (Key-Value)
* MongoDB (Document)
* Cassandra (Wide-Column)
* Neo4j (Graph)

---

## 🛠️ Prerequisites

* Docker installed: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* Docker Compose installed
* Python 3.8+ for Django Dashboard
* At least 4GB RAM (8GB recommended)

---

## ▶️ Getting Started

1. **Clone this project**

   ```bash
   git clone https://github.com/your-username/mini-cloud.git
   cd mini-cloud
   ```

2. **Start all services**
   Give execute permission to the `start-all.sh` script and run it:
   ```bash
   chmod +x start-all.sh
   ./start-all.sh
   ```

3. **Run Django Dashboard**

   ```bash
   pip install -r requirements.txt
   cd dashboard
   python manage.py runserver
   ```

4. **Access the dashboard at:** [http://localhost:8000](http://localhost:8000)

---

## 🛠️ Dashboard Development Setup

If you want to set up the Django dashboard from scratch, follow these steps:

1. **Create the Django project and app**
   ```bash
   django-admin startproject dashboard_project dashboard
   cd dashboard
   python manage.py startapp dashboard_app
   ```

2. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

3. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## 🧼 Stop All Services

```bash
docker-compose down
```

## 🔄 Rebuild After Changes

```bash
docker-compose up --build -d
```

---

## 📈 Optional Enhancements

* Use Traefik/Nginx for reverse proxy and HTTPS
* Use Heimdall or Dashy for visual dashboard (alternative)
* Mount external volumes for persistence
* Add Django admin features for CRUD on tool configurations

---

## 😍 Need Help?

Open an issue or contact the maintainer for support.

---

## 📝 License

MIT License - Free to modify and use.

---

Happy hosting! ☁️
