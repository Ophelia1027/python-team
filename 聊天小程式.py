from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.clock import Clock
import random

LabelBase.register(name="MSJhengHei", fn_regular="C:/Windows/Fonts/msjh.ttc")

class ChatBotUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        Window.clearcolor = (0.98, 0.94, 0.92, 1)  # 淺米色背景

        self.chat_log = Label(
            text="🌞 Loney：嗨嗨～我是你的陽光聊天夥伴，有我在，就不孤單了 ☀️\n",
            font_name="MSJhengHei",
            color=(0, 0, 0, 1),
            size_hint_y=8,
            halign='left',
            valign='top',
        )
        self.chat_log.bind(size=self.update_label_size)
        self.add_widget(self.chat_log)

        self.user_input = TextInput(
            hint_text="跟 Loney 說說話吧～",
            multiline=False,
            font_name="MSJhengHei",
            foreground_color=(0, 0, 0, 1),
            size_hint_y=1,
        )
        self.user_input.bind(on_text_validate=self.send_message)
        self.add_widget(self.user_input)

        self.send_button = Button(
            text="傳送 💌",
            font_name="MSJhengHei",
            size_hint_y=1
        )
        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)

    def update_label_size(self, *args):
        self.chat_log.text_size = (self.chat_log.width, None)
        self.chat_log.texture_update()
        self.chat_log.height = self.chat_log.texture_size[1]

    def send_message(self, instance):
        user_text = self.user_input.text.strip()
        if user_text == "":
            return
        self.chat_log.text += f"\n你：{user_text}"
        self.user_input.text = ""
        self.update_label_size()

        reply = self.get_reply(user_text)
        self.chat_log.text += f"\nLoney：{reply}\n"
        self.update_label_size()

    def get_reply(self, user_text):
        text = user_text.lower()

        # 判斷「沒有」或否定句
        negative_phrases = ["沒有", "沒", "沒有啦", "沒啊", "沒有哦", "沒有喔"]
        if any(neg in text for neg in negative_phrases):
            replies = [
                "沒關係，慢慢來，我陪著你！🌞",
                "沒什麼也沒關係，重要的是你還在這裡～",
                "有時候什麼都沒有，反而是新的開始！☀️",
                "沒關係，隨時都可以跟我聊喔！😊"
            ]
            return random.choice(replies)

        if any(word in text for word in ["你好", "哈囉", "嗨", "hello"]):
            return "嗨！希望你今天過得愉快！🌞"
        elif any(word in text for word in ["天氣", "氣候"]):
            return "今天天氣不錯，適合出去走走喔！☀️"
        elif any(word in text for word in ["心情", "感覺", "開心", "難過", "累", "疲憊", "孤單", "失落"]):
            if any(word in text for word in ["難過", "累", "疲憊", "孤單", "失落"]):
                replies = [
                    "沒關係，陰天過後一定會有陽光🌈，我陪你喔！",
                    "難過的時候記得深呼吸，小太陽永遠在你心裡！☀️",
                    "我在這裡陪著你，不要害怕孤單😊",
                    "哭一哭也沒關係，感情像太陽一樣，會溫暖你！"
                ]
                return random.choice(replies)
            else:
                return "跟我說說你的心情吧，我很願意聆聽！🌻"
        elif any(word in text for word in ["興趣", "嗜好", "喜歡做"]):
            return "我喜歡陪你聊天，你呢？有什麼興趣分享嗎？😊"
        elif any(word in text for word in ["工作", "上班", "公司", "學校", "讀書"]):
            return "工作和學習雖然辛苦，但也很充實，加油！🌟"
        elif any(word in text for word in ["旅遊", "旅行", "假期", "景點"]):
            return "旅行是放鬆的好方法，有沒有想去的地方呢？✈️"
        elif any(word in text for word in ["美食", "吃", "餐廳", "食物", "料理"]):
            return "美食真是療癒的良藥！最近有沒有什麼好吃的推薦？🍰"
        elif any(word in text for word in ["電影", "音樂", "歌", "唱片", "看電影"]):
            return "電影和音樂是生活的調味品，你最近看過什麼好電影嗎？🎬"
        elif any(word in text for word in ["再見", "bye", "掰掰", "回頭見"]):
            return "再見囉！期待下次聊天！🌞"
        else:
            fallback = [
                "嗯嗯，能再說詳細一點嗎？🌻",
                "哎呀，我還在學習中，你能教我更多嗎？🌞",
                "有趣！能不能再告訴我一些？😊",
                "我聽不太懂，可以換個說法嗎？🌈"
            ]
            return random.choice(fallback)

class LoneyApp(App):
    def build(self):
        return ChatBotUI()

if __name__ == "__main__":
    LoneyApp().run()
