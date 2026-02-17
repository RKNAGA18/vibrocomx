from unheard_voices.components.base import BaseComponent
from unheard_voices.components.layout import MainLayout
from unheard_voices.components.widgets import NextTalkWidget, NewsTicker
from unheard_voices.components.blog import BlogList
from unheard_voices import settings

class HomePage(BaseComponent):
    def render(self) -> str:
        # Mock Data
        ticker_items = [
            "Global South unites against sanctions",
            "Whistleblower reveals new surveillance tactics",
            "Independent media under attack in Europe",
            "Resource wars: The hidden truth",
            "Julian Assange's legacy continues"
        ]
        
        latest_articles = [
            {
                "title": "The Silent war in the Congo",
                "summary": "While the world watches elsewhere, corporations are fueling a conflict that has claimed millions of lives. We expose the supply chain.",
                "image_url": "",
                "category": "Field Report",
                "link": "/article/congo-silent-war"
            },
            {
                "title": "De-dollarization: A new era?",
                "summary": "Analysis of the BRICS summit and what it means for the future of western economic hegemony.",
                "image_url": "",
                "category": "Analysis",
                "link": "/article/dedollarization"
            },
            {
                "title": "Media Blackout on Protests",
                "summary": "Thousands march in the capital, but you won't see it on the evening news. Our on-the-ground report.",
                "image_url": "",
                "category": " censorship",
                "link": "/article/protests-blackout"
            }
        ]

        # Component Assembly
        ticker = NewsTicker(headlines=ticker_items)
        hero_section = f"""
        <section class="mb-12 text-center py-20 bg-gradient-to-b from-gray-900 to-slate-900 border-b border-gray-800">
            <h1 class="text-5xl md:text-7xl font-black text-white mb-6 uppercase tracking-tighter">
                Give Voice to the <span class="text-red-600">Unheard</span>
            </h1>
            <p class="text-xl md:text-2xl text-gray-400 max-w-3xl mx-auto leading-relaxed">
                Challenging the mainstream narrative. Exposing the injustices ignored by western media.
                <strong class="text-white block mt-2">Truth is our only agenda.</strong>
            </p>
            <div class="mt-8">
                <a href="/about" class="bg-red-600 text-white font-bold py-3 px-8 rounded hover:bg-red-700 transition-colors uppercase tracking-widest text-sm">
                    Our Mission
                </a>
            </div>
        </section>
        """
        
        next_talk = NextTalkWidget(
            speaker="Dr. Ayesha Khan",
            topic="Neo-Colonialism in the Digital Age",
            time="04:23:12"
        )
        
        blog_preview = BlogList(articles=latest_articles)

        content = [
            ticker,
            NextTalkWidget(speaker="Dr. Ayesha Khan", topic="Neo-Colonialism in the Digital Age", time="04:23:12"), # Using component directly in layout for simplicity in rendering? No, pass keys.
            # Actually I can just pass the string rendered content or the component itself if MainLayout handled it.
            # But MainLayout takes children components.
            # Let's wrap raw HTML strings in a helper or just make HomePage return the full HTML.
        ]
        
        # To strictly follow the component pattern, I'd wrap the Hero in a component, but string injection is fine for this demo.
        # Let's compose the body content.
        
        body_content = f"{ticker.render()}{hero_section}{next_talk.render()}{blog_preview.render()}"
        
        # MainLayout expects components, but we can make a 'RawHTML' component or just pass a list of things that have .render()
        # For simplicity of this `render` method, I will return the MainLayout rendered string.
        
        # We need a generic wrapper to pass the string content to MainLayout if MainLayout iterates children.
        class RawContent(BaseComponent):
            def __init__(self, html): self.html = html
            def render(self): return self.html
            
        layout = MainLayout(
            title="Home",
            children=[RawContent(body_content)]
        )
        return layout.render()
