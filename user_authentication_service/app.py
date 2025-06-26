#!/usr/bin/env python3
"""Basic Flask app"""
from auth import Auth
from flask import Flask, jsonify, abort, request, redirect
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


@app.route('/logout', methods=['DELETE'])
def logout():
    """Log a user out"""
    try:
        session_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect('/')
        else:
            abort(403)
    except Exception:
        abort(403)


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


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Reset a password token"""
    try:
        email = request.form.get('email')
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Update a user's password"""
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        new_password = request.form.get('new_password')
        AUTH.update_password(reset_token, new_password)
        if AUTH.valid_login(email, new_password):
            return jsonify(
                {"email": email,
                 "message": "Password updated"}), 200
        else:
            abort(403)
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
