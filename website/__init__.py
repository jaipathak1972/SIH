from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfkjdkfd fjkdfdjkfjdkd fddfdd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ahmed#2909@localhost/speechcare'

    db.init_app(app)

    # Register blueprints (ensure auth has login and register routes)
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    # Import models
    from .models import User

    # Create the database
    with app.app_context():
        db.create_all()

    # Setup Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Route for the home page
    @app.route('/')
    def home():
        return render_template('index.html')  # Render the home page

    return app
