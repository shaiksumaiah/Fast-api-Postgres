# FastAPI + PostgreSQL Project

This project is a FastAPI application with PostgreSQL, fully containerized using Docker Compose, ready to deploy on AWS EC2.

---

## Features
- CRUD operations for items
- SQLAlchemy ORM models
- Pydantic schemas
- Dockerized for easy deployment
- Ready for cloud deployment on AWS

---

## Folder Structure

fastapi-postgres/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── README.md


---

## Running Locally / On EC2

```bash
docker compose up --build -d
FastAPI Swagger UI: http://localhost:8000/docs (or <EC2_PUBLIC_IP>:8000/docs after deployment)

Postgres access:

docker exec -it fastapi-postgres-db-1 psql -U postgres -d fastapi
API Endpoints
Method	Path	Description
GET	/items/	List all items
POST	/items/	Create a new item
GET	/items/{id}	Retrieve single item
PUT	/items/{id}	Update item
DELETE	/items/{id}	Delete item
Deployment on AWS EC2

Launch an EC2 instance (Ubuntu 22.04 LTS)

Install Docker & Docker Compose

Copy the project to EC2

Run docker compose up --build -d

Access Swagger UI at http://<EC2_PUBLIC_IP>:8000/docs

Requirements

Python 3.9+

FastAPI

SQLAlchemy

psycopg2-binary

Docker & Docker Compose

Author

Shaik Sumaiah


---

# **Step 2 — Add README.md to your project**

1. Make sure `README.md` is saved in your **project root**:


fastapi-postgres/
│── README.md
│── docker-compose.yml
│── Dockerfile
│── main.py
│── ... other files


---

# **Step 3 — Initialize Git and commit files**

Open terminal inside your project folder:

```bash
# Initialize Git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit with project and README"

Step 4 — Create GitHub repository

Go to GitHub
 → click New Repository

Name it fastapi-postgres

Optional: add description, keep it public or private

Do not initialize with README (we already have one locally)

Click Create Repository

Step 5 — Link local repo to GitHub and push
# Replace <username> with your GitHub username
# Replace <repo> with repository name
git remote add origin https://github.com/<username>/fastapi-postgres.git

# Push local commits to GitHub
git branch -M main
git push -u origin main

✅ Done!

Your project now has a README.md

The project is version-controlled with Git

The code and README are on GitHub

