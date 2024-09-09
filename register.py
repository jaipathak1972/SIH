from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

# MySQL connection config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jaipathak2005@localhost/speechcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

db = SQLAlchemy(app)

# User model with all fields from the registration form
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

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        password = request.form['password']
        gender = request.form['gender']
        medical_history = request.form['medical_history']
        emergency_contact = request.form['emergency_contact']
        therapy_goals = request.form['therapy_goals']
        progress_notes = request.form['progress_notes']

        # Create a new user object and add to the database
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            password=password,  # Password will be hashed
            gender=gender,
            medical_history=medical_history,
            emergency_contact=emergency_contact,
            therapy_goals=therapy_goals,
            progress_notes=progress_notes
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query user by email
        user = User.query.filter_by(email=email).first()

        # Check if the user exists and password matches
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
