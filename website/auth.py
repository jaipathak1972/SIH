from flask import Blueprint, render_template, redirect, url_for, flash, request,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query user by email
        user = User.query.filter_by(email=email).first()

        # Check if the user exists and password matches
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect(url_for('auth.dashboard'))
        else:
            return redirect(url_for('auth.dashboard'))

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
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

        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    
    return redirect(url_for('login'))

@auth.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))
