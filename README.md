# 🧪 API Load Testing with Locust

This project demonstrates how to simulate API traffic and measure performance using **Locust**, a modern load testing tool for Python.

## 🔍 What It Does

- Sends concurrent requests to a sample API endpoint
- Measures latency, throughput, and request failures
- Provides a real-time web dashboard for monitoring

## 🧰 Stack

- Python 3
- Locust

## 📂 Project Structure

```
api-load-testing/
├── locustfile.py
├── requirements.txt
└── README.md
```

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Locust

```bash
locust
```

### 3. Open Web UI

Visit: [http://localhost:8089](http://localhost:8089)  
Enter:
- Host: your API base URL (e.g., `http://localhost:5000`)
- Number of users and spawn rate

---

> Ideal for testing performance of REST APIs, microservices, and web apps.
