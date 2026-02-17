from .base import BaseComponent
from unheard_voices import settings

class NextTalkWidget(BaseComponent):
    def __init__(self, speaker: str, topic: str, time: str):
        super().__init__()
        self.speaker = speaker
        self.topic = topic
        self.time = time

    def render(self) -> str:
        return f"""
        <div class="border-2 {settings.THEME_COLORS['accent_border']} p-6 my-6 bg-black/50 rounded-lg shadow-lg relative overflow-hidden group">
            <div class="absolute top-0 right-0 bg-red-600 text-white text-xs font-bold px-3 py-1 uppercase tracking-widest">
                Upcoming Live
            </div>
            <h3 class="{settings.THEME_COLORS['text_muted']} text-sm uppercase tracking-widest mb-2">Next Broadcast</h3>
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center">
                <div>
                    <h2 class="text-2xl md:text-3xl font-bold text-white mb-1">{self.topic}</h2>
                    <p class="{settings.THEME_COLORS['accent_text']} font-semibold text-lg">with {self.speaker}</p>
                </div>
                <div class="mt-4 md:mt-0 text-right">
                     <span class="block text-4xl font-black font-mono text-white tracking-widest">{self.time}</span>
                     <span class="text-xs text-gray-400">Time Remaining</span>
                </div>
            </div>
        </div>
        """

class NewsTicker(BaseComponent):
    def __init__(self, headlines: list):
        super().__init__()
        self.headlines = headlines

    def render(self) -> str:
        items = " &bull; ".join(self.headlines)
        return f"""
        <div class="bg-red-900/20 border-y border-red-900/50 py-2 overflow-hidden mb-8">
            <div class="whitespace-nowrap animate-marquee">
                <span class="mx-4 text-red-200 font-mono text-sm uppercase tracking-wide">
                    BREAKING: {items}
                </span>
            </div>
        </div>
        <style>
            .animate-marquee {{
                animation: marquee 20s linear infinite;
            }}
            @keyframes marquee {{
                0% {{ transform: translateX(100%); }}
                100% {{ transform: translateX(-100%); }}
            }}
        </style>
        """
