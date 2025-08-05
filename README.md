# 🧰 Docker-s-Mini-Cloud - 15+ GUI Tools
It provides a self-hosted "mini cloud" environment using Docker Compose, including 15+ open-source GUI-based tools for development, monitoring, file management, and infrastructure services.

---

## 📁 Directory Structure

```
mini-cloud/
├── docker-compose.yml
├── nginx/
│   └── default.conf (optional for reverse proxy)
├── prometheus.yml (for Prometheus config)
├── README.md
└── dashboard.html (optional: simple landing page for your tools)
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

## 🛠️ Prerequisites

* Docker installed: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* Docker Compose installed
* At least 4GB RAM (8GB recommended)

---

## ▶️ Getting Started

1. **Clone this project**

   ```bash
   git clone https://github.com/your-username/mini-cloud.git
   cd mini-cloud
   ```

2. **Start all services**

   ```bash
   docker-compose up -d
   ```

3. **Access the tools in your browser**

| Tool        | URL                                              |
| ----------- | ------------------------------------------------ |
| Portainer   | [http://localhost:9000](http://localhost:9000)   |
| Adminer     | [http://localhost:8080](http://localhost:8080)   |
| pgAdmin     | [http://localhost:5050](http://localhost:5050)   |
| MinIO       | [http://localhost:9001](http://localhost:9001)   |
| FileBrowser | [http://localhost:8081](http://localhost:8081)   |
| Code-Server | [http://localhost:8443](http://localhost:8443)   |
| NocoDB      | [http://localhost:8082](http://localhost:8082)   |
| Appsmith    | [http://localhost:8083](http://localhost:8083)   |
| Grafana     | [http://localhost:3001](http://localhost:3001)   |
| Prometheus  | [http://localhost:9090](http://localhost:9090)   |
| Netdata     | [http://localhost:19999](http://localhost:19999) |
| Uptime Kuma | [http://localhost:3002](http://localhost:3002)   |
| Vaultwarden | [http://localhost:8085](http://localhost:8085)   |
| Nextcloud   | [http://localhost:8086](http://localhost:8086)   |
| Gitea       | [http://localhost:3000](http://localhost:3000)   |

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

## 📌 Optional Enhancements

* Add a **reverse proxy** (e.g., Traefik or Nginx) for domain routing and HTTPS.
* Use **Heimdall**, **Flame**, or **Dashy** as a dashboard to link to all services.
* Connect external volumes for persistence.
* Enable **authentication** and **TLS** for production.

---

## 🙋 Need Help?

Feel free to open an issue in the repository or contact the maintainer.

---

## 📝 License

MIT License - Feel free to modify and use this project.

---

Happy hosting! ☁️
