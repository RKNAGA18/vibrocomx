# Main Application / Static Site Generator
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.home import HomePage
from pages.blog import BlogPage
from pages.about import AboutPage

OUTPUT_DIR = "."

def build_site():
    print("Building Unheard Voices...")
    
    pages = [
        ("index.html", HomePage()),
        ("blog.html", BlogPage()),
        ("about.html", AboutPage())
    ]
    
    for filename, page in pages:
        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(page.render())
        print(f"Generated: {output_path}")

    print("Build Complete.")

if __name__ == "__main__":
    build_site()
