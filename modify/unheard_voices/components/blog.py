from .base import BaseComponent
from unheard_voices import settings

class ArticleCard(BaseComponent):
    def __init__(self, title: str, summary: str, image_url: str, category: str, link: str = "#"):
        super().__init__()
        self.title = title
        self.summary = summary
        self.image_url = image_url
        self.category = category
        self.link = link

    def render(self) -> str:
        return f"""
        <div class="bg-slate-800 rounded-lg overflow-hidden hover:transform hover:-translate-y-1 transition-all duration-300 border border-slate-700">
            <div class="h-48 bg-slate-700 relative">
                <!-- Placeholder for image if not provided, or img tag -->
                <div class="absolute inset-0 flex items-center justify-center text-slate-500 bg-slate-900">
                    <span class="text-xs uppercase">Thumbnail: {self.category}</span>
                </div>
                <span class="absolute top-2 left-2 bg-red-600 text-white text-xs font-bold px-2 py-1 rounded">
                    {self.category}
                </span>
            </div>
            <div class="p-4">
                <h3 class="text-xl font-bold mb-2 text-white leading-tight">
                    <a href="{self.link}" class="hover:text-red-500 transition-colors">{self.title}</a>
                </h3>
                <p class="text-gray-400 text-sm mb-4 line-clamp-3">
                    {self.summary}
                </p>
                <a href="{self.link}" class="inline-block text-red-500 font-bold text-sm hover:underline uppercase tracking-wide">
                    Read Analysis &rarr;
                </a>
            </div>
        </div>
        """

class BlogList(BaseComponent):
    def __init__(self, articles: list):
        super().__init__()
        self.articles = articles

    def render(self) -> str:
        # Assuming articles is a list of dicts or objects that can be passed to ArticleCard
        grid_items = "".join([ArticleCard(**article).render() for article in self.articles])
        return f"""
        <section class="my-12">
            <h2 class="text-3xl font-black text-white mb-8 border-l-4 border-red-600 pl-4">Latest Analysis</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {grid_items}
            </div>
        </section>
        """
