# 🚀 Dockerized Python + PostgreSQL Application

This project demonstrates how to run a **Python (Flask) web application** with a
**PostgreSQL database** using **Docker and Docker Compose**.

---

## 📌 Prerequisites

- Ubuntu 20.04 / 22.04 (Local machine or EC2 instance)
- sudo privileges
- Internet connection

---

## 🐳 Step 1: Install Docker & Docker Compose

### Update system
```bash
sudo apt update
```

### Install required packages
```bash
sudo apt install -y ca-certificates curl gnupg lsb-release
```

### Add Docker GPG key
```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### Add Docker repository

```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker Engine & Compose plugin

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### Verify installation
```bash
docker --version
docker compose version
```

### 👤 Step 2: Run Docker Without sudo
```bash
sudo usermod -aG docker ubuntu
newgrp docker
docker ps
```

### 📁 Project Structure

project_2/

│

├── Dockerfile

├── app.py

├── docker-compose.yml

├── requirements.txt

└── README.md


