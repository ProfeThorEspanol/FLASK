from flask import Flask
from src.app.models.auth_model import db
from src.routes.web import auth_routes

app = Flask(__name__, template_folder='./../resources/views')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)

with app.app_context():
    db.create_all()

# Inicializamos las rutas
auth_routes(app)

def web_app(): return app