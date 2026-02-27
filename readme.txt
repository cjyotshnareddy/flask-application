# User API – Flask + SQLite

## Overview
Simple REST API built using Flask.
- SQLite database
- SQLAlchemy ORM
- JSON data loading
- CRUD operations
- Pagination, search, sorting
- Aggregation endpoint

---

## Setup Instructions

### 1. Clone / Download Project
cd user_api

### 2. Create Virtual Environment
python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install Dependencies
pip install -r requirements.txt

---

### 4. Run the Application
python app.py

Server runs at:
http://127.0.0.1:5000

---

## Available Endpoints

GET    /api/users
POST   /api/users
GET    /api/users/<id>
PUT    /api/users/<id>
DELETE /api/users/<id>
GET    /api/users/summary

---

## Notes
- SQLite DB file: users.db
- Comment load_data() after first run to avoid duplicate entries.

