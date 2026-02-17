from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from models import db, User, Post, PageContent, SocialLink, SiteSetting, Founder

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Login failed. Check username/password.', 'danger')
            
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    posts = Post.query.all()
    social_links = SocialLink.query.all()
    pages = PageContent.query.all()
    settings = SiteSetting.query.all() # Updated Model Name
    founders = Founder.query.all()
    
    return render_template('admin/dashboard.html', 
                           posts=posts, social_links=social_links, 
                           pages=pages, settings=settings, founders=founders)

@admin_bp.route('/toggle-setting/<setting_key>', methods=['POST'])
@login_required
def toggle_setting(setting_key):
    setting = SiteSetting.query.filter_by(setting_key=setting_key).first()
    if setting:
        new_value = 'false' if setting.setting_value == 'true' else 'true'
        setting.setting_value = new_value
        db.session.commit()
        flash(f'{setting_key} toggled to {new_value}', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/edit-page', methods=['POST'])
@login_required
def edit_page(): # Renamed from edit_page_content
    page_name = request.form.get('page_name')
    content = request.form.get('content')
    
    page = PageContent.query.filter_by(page_name=page_name).first()
    if not page:
        page = PageContent(page_name=page_name)
        db.session.add(page)
    
    page.content = content
    db.session.commit()
    flash(f'{page_name} content updated.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/manage-link', methods=['POST'])
@login_required
def manage_link():
    link_id = request.form.get('link_id')
    platform = request.form.get('platform')
    url = request.form.get('url')
    
    if link_id:
        link = SocialLink.query.get(link_id)
        if link:
            link.platform = platform
            link.url = url
    else:
        # Simple icon mapping logic or default
        icon_map = {
            'twitter': 'fab fa-twitter',
            'x': 'fab fa-twitter', # X is twitter icon usually
            'youtube': 'fab fa-youtube',
            'telegram': 'fab fa-telegram',
            'instagram': 'fab fa-instagram'
        }
        icon = icon_map.get(platform.lower(), 'fas fa-link')
        
        new_link = SocialLink(platform=platform, url=url, icon_class=icon)
        db.session.add(new_link)
        
    db.session.commit()
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete-link/<int:id>')
@login_required
def delete_link(id):
    link = SocialLink.query.get_or_404(id)
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for('admin.dashboard'))

# --- Founders Manager ---
@admin_bp.route('/manage-founder', methods=['POST'])
@login_required
def manage_founder():
    name = request.form.get('name')
    role = request.form.get('role')
    bio = request.form.get('bio')
    image_url = request.form.get('image_url')
    
    # Simple add for now (could extend to edit if id passed)
    founder = Founder(name=name, role=role, bio=bio, image_url=image_url)
    db.session.add(founder)
    db.session.commit()
    flash(f'Founder {name} added.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete-founder/<int:id>')
@login_required
def delete_founder(id):
    founder = Founder.query.get_or_404(id)
    db.session.delete(founder)
    db.session.commit()
    flash('Founder removed.', 'success')
    return redirect(url_for('admin.dashboard'))

# --- Post Manager ---
@admin_bp.route('/manage-post', methods=['POST'])
@login_required
def manage_post():
    title = request.form.get('title')
    slug = request.form.get('slug')
    summary = request.form.get('summary')
    content = request.form.get('content')
    category = request.form.get('category')
    image_url = request.form.get('image_url')
    
    if not slug:
        slug = title.lower().replace(' ', '-')
        
    post = Post(title=title, slug=slug, summary=summary, content=content, 
                category=category, image_url=image_url)
    db.session.add(post)
    db.session.commit()
    flash(f'Post "{title}" created.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete-post/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'success')
    return redirect(url_for('admin.dashboard'))
