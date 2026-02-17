from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
# Ensure 'models' is the name of your file containing the database classes
from models import db, User, Post, PageContent, SocialLink, SiteSetting, Founder

admin_bp = Blueprint('admin', __name__)

# --- Login Route ---
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    # If already logged in, send to dashboard
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Login failed. Check username/password.', 'danger')
            
    return render_template('login.html') # Make sure this matches your template folder structure

# --- Logout Route ---
@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) # Ensure 'index' exists in app.py

# --- Dashboard Route ---
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    posts = Post.query.all()
    social_links = SocialLink.query.all()
    pages = PageContent.query.all()
    settings = SiteSetting.query.all()
    founders = Founder.query.all()
    
    # Pass all these variables to the template
    return render_template('dashboard.html', 
                           posts=posts, 
                           social_links=social_links, 
                           pages=pages, 
                           settings=settings, 
                           founders=founders)
