from flask import Flask
from src.app.http.controllers.auth_controller import register, login, dashboard

def auth_routes(app:Flask):
    app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
    app.add_url_rule('/dashboard', view_func=dashboard, methods=['GET'])
