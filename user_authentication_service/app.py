#!/usr/bin/env python3
"""Basic Flask app"""
from auth import Auth
from flask import Flask, jsonify, abort, request
from os import getenv

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Return welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Register user if not already exists"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Log a user in"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response
        else:
            abort(401)
    except Exception:
        abort(401)


@app.route('/profile', methods=['GET'])
def profile():
    """Return a user profile"""
    try:
        session_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(session_id)
        if user is None:
            abort(403)
        email = user.email
        return jsonify({"email": email}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
