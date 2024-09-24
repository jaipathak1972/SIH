from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(255))
    role = db.Column(db.String(20))
    profile_pic = db.Column(db.String(255))
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    password_hash = db.Column(db.String(255))  # Storing hashed password
    gender = db.Column(db.String(10))
    medical_history = db.Column(db.Text)
    emergency_contact = db.Column(db.String(100))
    therapy_goals = db.Column(db.Text)
    progress_notes = db.Column(db.Text)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Constructor to initialize User
    def __init__(self, first_name, last_name, email, phone_number, address, password, gender, medical_history, emergency_contact, therapy_goals=None, progress_notes=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        # Store hashed password
        self.password_hash = generate_password_hash(password)  # Storing hashed password
        self.gender = gender
        self.medical_history = medical_history
        self.emergency_contact = emergency_contact
        self.therapy_goals = therapy_goals
        self.progress_notes = progress_notes

    # Check password hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)