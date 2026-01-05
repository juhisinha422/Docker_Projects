# Dockerized Flask Application

This repository contains a simple **Flask web application** that is containerized using **Docker**.  
It demonstrates how to build, run, and deploy a Python Flask app using Docker.

---

## 📁 Project Structure

Docker_Projects/

│── Dockerfile

│── app.py

│── requirements.txt

│── .gitignore

│── README.md


---

## 🚀 Application Overview

- Framework: **Flask**
- Language: **Python 3.9**
- Containerization: **Docker**
- Exposed Port: **5000**

When the application is running, it returns:
Hello, Docker!

---

## 🐳 Dockerfile Explanation

- Uses official `python:3.9` base image
- Installs dependencies from `requirements.txt`
- Copies application code into the container
- Exposes port `5000`
- Runs the Flask application

---

## ▶️ How to Run the Application

### 1️⃣ Clone the repository

```bash
git clone https://github.com/juhisinha422/Docker_Projects.git
cd Docker_Projects
```

### 2️⃣ Build the Docker image

```bash
docker build -t flask-app .
```

### 3️⃣ Run the Docker container

```bash 
docker run -p 5000:5000 flask-app
```

### 4️⃣ Access the application

Open your browser and visit:
```bash
http://localhost:5000

or (if running on EC2):

http://<EC2_PUBLIC_IP>:5000
```

### Optional

🧪 Test Using Curl
```bash
curl http://localhost:5000
```

Expected output: Hello, Docker!




