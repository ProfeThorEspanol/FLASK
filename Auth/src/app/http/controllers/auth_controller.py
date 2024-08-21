from flask import render_template, redirect, url_for, request, flash, session
from src.app.models.auth_model import db, User
from src.app.http.middleware.auth_middleware import login_required
  # Ajusta el import según tu estructura

def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash('El correo ya está en uso.', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email)#type:ignore
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login exitoso.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@login_required
def dashboard():
    return render_template('dashboard.html')