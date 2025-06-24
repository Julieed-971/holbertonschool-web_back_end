#!/usr/bin/env python3
"""Module of session auth views"""
from api.v1.views import app_views
from flask import jsonify, request, make_response
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """POST /api/v1/auth_session/login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or email is None:
        return jsonify({"error": "email missing"}), 400
    if not password or password is None:
        return jsonify({"error": "password missing"}), 400
    user = User()
    user.load_from_file()
    found_user = user.search({'email': email})
    if not found_user:
        return jsonify({"error": "no user found for this email"}), 404
    if not found_user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    user_id = found_user[0].id
    session_id = auth.create_session(user_id)
    cookie_name = getenv("SESSION_NAME")
    response = make_response(found_user[0].to_json(True))
    response.set_cookie(cookie_name, session_id)
    return response
