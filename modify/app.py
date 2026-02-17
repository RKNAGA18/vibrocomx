from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, current_user
import os
from models import db, User, Post, PageContent, SocialLink, SiteSetting, Founder
from admin_routes import admin_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vibrocomx-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vibrocomx.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_globals():
    social_links = SocialLink.query.all()
    
    banner_setting = SiteSetting.query.filter_by(setting_key='breaking_banner').first()
    show_banner = banner_setting.setting_value == 'true' if banner_setting else True
    
    breaking_text_setting = SiteSetting.query.filter_by(setting_key='breaking_text').first()
    breaking_text = breaking_text_setting.setting_value if breaking_text_setting else "Global South unites against sanctions"
    
    return dict(social_links=social_links, show_banner=show_banner, breaking_text=breaking_text)

@app.route('/')
def index():
    mnt_setting = SiteSetting.query.filter_by(setting_key='maintenance_mode').first()
    if mnt_setting and mnt_setting.setting_value == 'true' and not current_user.is_authenticated:
        return render_template('maintenance.html')

    posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()
    return render_template('index.html', posts=posts)

@app.route('/mission')
def mission():
    content = PageContent.query.filter_by(page_name='mission').first()
    founders = Founder.query.all()
    mission_text = content.content if content else "Mission content not set."
    return render_template('mission.html', mission_text=mission_text, founders=founders)

@app.route('/analysis')
def analysis():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('posts.html', posts=posts, title="Analysis")

@app.route('/article/<slug>')
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('article.html', post=post)

# Register Blueprint
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
