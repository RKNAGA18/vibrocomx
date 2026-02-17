from app import app, db
from models import User, SiteSetting, PageContent, SocialLink, Post, Founder
from werkzeug.security import generate_password_hash
from datetime import datetime

def init_db():
    with app.app_context():
        # Drop everything for a fresh start so we get the new posts
        db.drop_all()
        db.create_all()

        # Create Admin
        if not User.query.filter_by(username='admin').first():
            hashed_pw = generate_password_hash('vibrocomx', method='pbkdf2:sha256')
            admin = User(username='admin', password=hashed_pw)
            db.session.add(admin)
            print("Admin user created (admin/vibrocomx)")

        # Default Settings
        settings = [
            ('maintenance_mode', 'false'),
            ('breaking_banner', 'true'),
            ('breaking_text', 'BREAKING: VibrocomX Exclusive: Global South unites against sanctions • Whistleblower reveals new surveillance tactics')
        ]
        
        for key, value in settings:
            if not SiteSetting.query.filter_by(setting_key=key).first():
                db.session.add(SiteSetting(setting_key=key, setting_value=value))
        
        # Default Mission
        if not PageContent.query.filter_by(page_name='mission').first():
            db.session.add(PageContent(page_name='mission', content='<p>We are the signal in the noise. While mainstream media manufactures consent, we deconstruct the narrative. <b>VibrocomX</b> is not just a platform; it is a movement.</p><p>Focusing on the Global South, economic warfare, and digital sovereignty.</p>'))

        # Default Social Link
        if not SocialLink.query.first():
            db.session.add(SocialLink(platform='Twitter/X', url='https://x.com', icon_class='fab fa-twitter'))
            db.session.add(SocialLink(platform='Telegram', url='https://t.me', icon_class='fab fa-telegram'))

        # Create Sample Posts (Using Generated Images)
        # Note: We assume the images are saved in the artifacts folder, but for the app to serve them 
        # normally they should be in static/images. 
        # Since I cannot move files easily with existing tools effectively without knowing exact paths or using shell,
        # I will point to them assuming they will be moved or I will reference them directly if possible.
        # Actually, best practice: user manually moves them, OR I use a relative path if I can save to static.
        # The generate_image tool saves to artifacts. I will use a placeholder or assume user copies them.
        # WAIT: I can just use the absolute path for now in the DB for local rendering.
        
        # NOTE: Update these paths if you move the files!
        posts = [
            {
                "title": "The Silent War in the Congo",
                "slug": "congo-silent-war",
                "summary": "While the world watches elsewhere, corporations are fueling a conflict that has claimed millions of lives. We expose the supply chain.",
                "content": "<p>Full report coming soon...</p>",
                "category": "Field Report",
                "image_url": "https://picsum.photos/seed/congo/800/400"
            },
            {
                "title": "De-dollarization: A new era?",
                "slug": "dedollarization",
                "summary": "Analysis of the BRICS summit and what it means for the future of western economic hegemony.",
                "content": "<p>Full analysis...</p>",
                "category": "Analysis",
                "image_url": "https://picsum.photos/seed/brics/800/400"
            },
            {
                "title": "Media Blackout on Protests",
                "slug": "protests-blackout",
                "summary": "Thousands march in the capital, but you won't see it on the evening news. Our on-the-ground report.",
                "content": "<p>On the ground...</p>",
                "category": "Censorship",
                "image_url": "https://picsum.photos/seed/protest/800/400"
            }
        ]

        for p_data in posts:
             if not Post.query.filter_by(slug=p_data['slug']).first():
                 post = Post(
                     title=p_data['title'],
                     slug=p_data['slug'],
                     summary=p_data['summary'],
                     content=p_data['content'],
                     category=p_data['category'],
                     image_url=p_data['image_url'],
                     date_posted=datetime.utcnow()
                 )
                 db.session.add(post)

        db.session.commit()
        print("Database Initialized Successfuly with Content!")

if __name__ == '__main__':
    init_db()
