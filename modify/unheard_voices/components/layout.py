from .base import BaseComponent, Container, Text
from unheard_voices import settings

class Navbar(BaseComponent):
    def render(self) -> str:
        return f"""
        <nav class="{settings.THEME_COLORS['secondary_bg']} border-b {settings.THEME_COLORS['accent_border']} p-4">
            <div class="container mx-auto flex justify-between items-center">
                <a href="/" class="text-2xl font-bold {settings.THEME_COLORS['accent_text']} uppercase tracking-wider">
                    {settings.SITE_NAME}
                </a>
                <div class="space-x-4">
                    <a href="/" class="{settings.THEME_COLORS['text_main']} hover:{settings.THEME_COLORS['accent_text']}">Home</a>
                    <a href="/blog" class="{settings.THEME_COLORS['text_main']} hover:{settings.THEME_COLORS['accent_text']}">Analysis</a>
                    <a href="/about" class="{settings.THEME_COLORS['text_main']} hover:{settings.THEME_COLORS['accent_text']}">Mission</a>
                </div>
            </div>
        </nav>
        """

class Footer(BaseComponent):
    def render(self) -> str:
        return f"""
        <footer class="{settings.THEME_COLORS['secondary_bg']} p-8 mt-12 border-t border-gray-800">
            <div class="container mx-auto text-center">
                <p class="{settings.THEME_COLORS['text_muted']}">
                    &copy; 2024 {settings.SITE_NAME}. All rights reserved.
                </p>
                <div class="mt-4 space-x-4">
                     <!-- Social Media Hub Placeholder -->
                    <a href="#" class="{settings.THEME_COLORS['text_main']}">Twitter/X</a>
                    <a href="#" class="{settings.THEME_COLORS['text_main']}">Telegram</a>
                    <a href="#" class="{settings.THEME_COLORS['text_main']}">Substack</a>
                </div>
            </div>
        </footer>
        """

class MainLayout(BaseComponent):
    def __init__(self, title: str, children: list):
        super().__init__(children=children)
        self.title = title

    def render(self) -> str:
        content = "".join([child.render() for child in self.children])
        return f"""
        <!DOCTYPE html>
        <html lang="en" class="dark">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.title} | {settings.SITE_NAME}</title>
            {settings.TAILWIND_CDN}
            <style>
                body {{ font-family: 'Inter', sans-serif; }}
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
            </style>
        </head>
        <body class="{settings.THEME_COLORS['primary_bg']} {settings.THEME_COLORS['text_main']} flex flex-col min-h-screen">
            {Navbar().render()}
            <main class="flex-grow container mx-auto px-4 py-8">
                {content}
            </main>
            {Footer().render()}
        </body>
        </html>
        """
