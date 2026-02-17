from unheard_voices.components.base import BaseComponent
from unheard_voices.components.layout import MainLayout

class AboutPage(BaseComponent):
    def render(self) -> str:
        class RawContent(BaseComponent):
            def __init__(self, html): self.html = html
            def render(self): return self.html

        content = """
        <div class="max-w-4xl mx-auto py-12">
            <h1 class="text-5xl font-black text-white mb-8">Our Mission</h1>
            <div class="prose prose-invert prose-lg text-gray-300">
                <p class="lead text-2xl text-white font-bold mb-6">
                    We exist to tell the stories that the mainstream media ignores, suppresses, or distorts.
                </p>
                <p>
                    In a world dominated by a handful of corporate media conglomerates, the truth is often the first casualty. 
                    <b>Unheard Voices</b> is an independent platform dedicated to investigative journalism, critical analysis, and field reporting from the forgotten corners of the globe.
                </p>
                <h3 class="text-2xl text-white font-bold mt-8 mb-4">Why We Are Here</h3>
                <ul class="list-disc pl-6 space-y-2 mb-8">
                    <li>To challenge western-centric narratives.</li>
                    <li>To highlight struggles against imperialism and neo-colonialism.</li>
                    <li>To provide a platform for independent thinkers and whistleblowers.</li>
                </ul>
                <div class="bg-red-900/20 border-l-4 border-red-600 p-6 my-8">
                    <p class="text-red-200 font-bold italic">
                        "Until the lion learns how to write, every story will glorify the hunter."
                    </p>
                </div>
            </div>
        </div>
        """
        
        return MainLayout(title="Mission", children=[RawContent(content)]).render()
