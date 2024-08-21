from flask import redirect, url_for, session, flash
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrap_login(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión primero.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrap_login