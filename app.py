from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import os
from sqlalchemy import func

app = Flask(__name__) #creating flask app and starting backend


# Database Configuration

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" #create database file named user.db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) #connecting database to flask app



# Database Model

class User(db.Model):  #creating a table user and the below each line is the each column in the table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zip = db.Column(db.String(20))
    email = db.Column(db.String(120),unique=True)
    web = db.Column(db.String(120))



# Helper: Convert User(object) to Dict
#first object then dict then json, database returns objects and this is a function to convert objects to dictionary
def user_to_dict(user):
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "company_name": user.company_name,
        "age": user.age,
        "city": user.city,
        "state": user.state,
        "zip": user.zip,
        "email": user.email,
        "web": user.web
    }


# Load JSON Data 

def load_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "users.json")

    with open(file_path) as f:
        users = json.load(f)

    for u in users:
        # Check if email already exists
        existing_user = User.query.filter_by(email=u["email"]).first()

        if not existing_user:
            user = User(**u)
            db.session.add(user)

    db.session.commit()


# GET All Users
#get = http://127.0.0.1:5000/api/users
#page = http://127.0.0.1:5000/api/users?page=1&limit=5
#search = http://127.0.0.1:5000/api/users?search=Rahul
#sort = http://127.0.0.1:5000/api/users?sort=age
#city = http://127.0.0.1:5000/api/users?city=Ban
#city =. query = query.filter(User.city.ilike(f"%{city}%"))
#delete  http://127.0.0.1:5000/api/users/3



@app.route("/api/users", methods=["GET"])
def get_users():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 5))
    search = request.args.get("search", "")
    sort = request.args.get("sort", "id")
    city = request.args.get("city", "")
  #starts database query
    query = User.query

    # Search by first or last name
    if search:
        query = query.filter(
            (User.first_name.ilike(f"%{search}%")) |
            (User.last_name.ilike(f"%{search}%"))
        )

    # Partial city filter
    if city:
        query = query.filter(User.city.ilike(f"%{city}%"))

    # Sorting
    if sort.startswith("-"):
        query = query.order_by(getattr(User, sort[1:]).desc())
    else:
        query = query.order_by(getattr(User, sort))

    users = query.paginate(page=page, per_page=limit)

    return jsonify([user_to_dict(u) for u in users.items])



# POST Create User

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    #creating new databse row
    user = User(**data)
    #saving to database
    db.session.add(user)
    db.session.commit()

    return jsonify(user_to_dict(user)), 201



# GET User by ID

@app.route("/api/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user_to_dict(user))


# PUT (Full Update)

@app.route("/api/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json

    for key in data:
        setattr(user, key, data[key])

    db.session.commit()
    return jsonify(user_to_dict(user))



# PATCH (Partial Update)

@app.route("/api/users/<int:id>", methods=["PATCH"])
def patch_user(id):
    user = User.query.get_or_404(id)
    data = request.json

    for key in data:
        setattr(user, key, data[key])

    db.session.commit()
    return jsonify(user_to_dict(user))



# DELETE

@app.route("/api/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted"}



# SUMMARY

@app.route("/api/users/summary", methods=["GET"])
def summary():
    count_by_city = db.session.query(
        User.city, func.count(User.id)
    ).group_by(User.city).all()

    avg_age = db.session.query(func.avg(User.age)).scalar()

    return jsonify({
        "count_by_city": dict(count_by_city),
        "average_age": avg_age
    })



# Run App

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        load_data()

    app.run(debug=True)