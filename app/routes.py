from flask import render_template, redirect, url_for, flash
from flask_login import (
    login_user, 
    logout_user, 
    login_required, 
    current_user
)
from app.models import User, Product
from app.forms import LoginForm

def init_routes(app):
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            products = Product.query.all()
            return render_template('index.html', products=products)
        return render_template('home/index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('index'))  
            flash('Identifiants invalides')
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))  

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404