from flask import Blueprint, jsonify
from .models import User
from .extensions import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return jsonify(message="Production Flask App Running 🚀")

@main_bp.route("/users")
def users():
    users = User.query.all()
    return jsonify([u.name for u in users])