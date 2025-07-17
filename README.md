# FlaskApp2 - Simple User Registration App

This is a minimal Flask web app that allows users to register with a username and password via an HTML form. Registered users are displayed immediately on the same page. All data is stored in memory (no database), making it great for demos, DevOps practice, and local container-based testing.

---

## ✨ Features

- 🧾 HTML form for user registration
- 👤 Stores usernames and passwords in memory (temporary)
- 👁 View all registered usernames on the homepage
- 🐳 Docker-ready

---

## 🐳 How to Run (Docker Only)

### 🔧 1. Build the Docker Image
```bash
docker build -t flaskapp2 .

