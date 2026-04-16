# 🚀 K8s Microservice Deployment System

A complete microservice-based application deployed using **Docker** and **Kubernetes (Minikube)**. This project demonstrates containerization, orchestration, and scalable deployment of a Python-based application.

---

## 📌 Project Overview

This project showcases how to:
- Containerize an application using Docker
- Deploy it on Kubernetes
- Manage services and scaling using K8s
- Build a basic microservice architecture

---

## 🛠️ Tech Stack

- 🐍 Python
- 🐳 Docker
- ☸️ Kubernetes (Minikube)
- 📦 YAML (K8s configuration)

---

## 📂 Project Structure
```
k8s-microservice/
│
├── app/
│ ├── main.py
│ └── requirements.txt
│
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
│
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

1. Python app is containerized using Docker  
2. Docker image is deployed on Kubernetes  
3. Deployment manages pods (replicas)  
4. Service exposes the application  

---

## 🚀 Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/subhedarharshal1-stack/k8s-microservice.git
cd k8s-microservice
```
### 2️⃣ Start Minikube
```
minikube start
```
### 3️⃣ Build Docker Image
```
docker build -t k8s-microservice .
```
### 4️⃣ Deploy to Kubernetes
```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
### 5️⃣ Check Pods & Services
```
kubectl get pods
kubectl get services
```
### 6️⃣ Access Application
```
minikube service k8s-service
```
---

## 📊 Features
- Containerized microservice architecture
- Kubernetes deployment & service management
- Scalable and modular design
- Easy setup using Minikube

---

## 🧠 Learning Outcomes
- Understanding Docker containerization
- Kubernetes architecture (Pods, Services, Deployments)
- Real-world microservice deployment
- DevOps fundamentals

--- 

## 👨‍💻 Author

Harshal Subhedar
B.sc Cloud Computing
