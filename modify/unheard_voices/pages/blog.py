from unheard_voices.components.base import BaseComponent
from unheard_voices.components.layout import MainLayout
from unheard_voices.components.blog import BlogList

class BlogPage(BaseComponent):
    def render(self) -> str:
        articles = [
            {"title": "The Silent war in the Congo", "summary": "...", "image_url": "", "category": "Field Report"},
            {"title": "De-dollarization: A new era?", "summary": "...", "image_url": "", "category": "Analysis"},
            {"title": "Media Blackout on Protests", "summary": "...", "image_url": "", "category": "censorship"},
            {"title": "Water Wars 2025", "summary": "Investigating the privatization of water resources.", "image_url": "", "category": "Environment"},
            {"title": "The Debt Trap", "summary": "How IMF loans cripple developing nations.", "image_url": "", "category": "Economy"},
            {"title": "Digital Sovereignty", "summary": "Building independent tech infrastructure.", "image_url": "", "category": "Tech"}
        ]
        
        class RawContent(BaseComponent):
            def __init__(self, html): self.html = html
            def render(self): return self.html

        content = f"""
        <div class="py-12">
            <h1 class="text-4xl font-black text-white mb-8 border-b border-gray-800 pb-4">All Investigations</h1>
            {BlogList(articles).render()}
        </div>
        """
        
        return MainLayout(title="Analysis", children=[RawContent(content)]).render()
