# dashboard_app/views.py

from django.shortcuts import render

def dashboard_view(request):
    tools = [
        {"name": "Portainer", "port": 9000, "description": "Docker GUI manager"},
        {"name": "Adminer", "port": 8080, "description": "Database admin tool"},
        {"name": "pgAdmin", "port": 5050, "description": "PostgreSQL admin GUI"},
        {"name": "FileBrowser", "port": 8081, "description": "Web-based file manager"},
        {"name": "Appsmith", "port": 8083, "description": "Low-code internal app builder"},
        {"name": "NocoDB", "port": 8082, "description": "Open-source Airtable alternative"},
        {"name": "Code Server", "port": 8443, "description": "VS Code in the browser"},
        {"name": "Grafana", "port": 3001, "description": "Metrics and dashboarding"},
        {"name": "Prometheus", "port": 9090, "description": "Monitoring system"},
        {"name": "Netdata", "port": 19999, "description": "System metrics dashboard"},
        {"name": "Uptime Kuma", "port": 3002, "description": "Self-hosted uptime monitor"},
        {"name": "Vaultwarden", "port": 8085, "description": "Password manager"},
        {"name": "Nextcloud", "port": 8086, "description": "Self-hosted cloud storage"},
        {"name": "Gitea", "port": 3000, "description": "Lightweight Git hosting"},
    ]
    return render(request, "index.html", {"tools": tools})
