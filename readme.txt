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




How long did it take you?

It took me around 5–6 hours overall. Some time went into setting up the environment and understanding how Flask connects to the database. The rest was building and testing the APIs properly.

What was most challenging?

The most challenging part was understanding how SQLAlchemy works behind the scenes — especially how the model class becomes a database table and how pagination actually limits results.

What was unclear?

Initially, I was a bit confused about how request handling works in Flask — especially how request.json connects to the database model. After experimenting a bit, it became clearer.

Any unexpected challenges?

Yes, I faced an issue where data was getting duplicated every time I ran the server because the JSON loader was executing on every run. I had to comment it out after the first execution.

Is the difficulty appropriate?

Yes, I think the difficulty level is appropriate. It’s a good balance between beginner and intermediate backend development. It covers real-world concepts like CRUD, pagination, and database integration.

Why did you choose these tools?

I chose Flask because it’s lightweight and easy to understand for building APIs. SQLite was chosen since it doesn’t require setting up a separate database server. SQLAlchemy makes database operations cleaner and avoids writing raw SQL.
Any assumptions or decisions made?

I assumed this was a development-level project, so I didn’t add advanced validation or authentication. I focused mainly on core API functionality and clean structure. I also chose simplicity over complexity to keep it readable and maintainable


https://flask.palletsprojects.com/en/stable/quickstart/