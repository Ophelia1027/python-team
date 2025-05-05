from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime
import random

class ChatBot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.chat_history = Label(size_hint_y=0.9, text="", valign="top", halign="left")
        self.chat_history.bind(size=self.update_text_width)
        self.add_widget(self.chat_history)

        self.input_area = BoxLayout(size_hint_y=0.1)
        self.user_input = TextInput(hint_text="輸入訊息...", multiline=False)
        self.send_button = Button(text="傳送")
        self.send_button.bind(on_press=self.send_message)

        self.input_area.add_widget(self.user_input)
        self.input_area.add_widget(self.send_button)
        self.add_widget(self.input_area)

    def update_text_width(self, *args):
        self.chat_history.text_size = (self.chat_history.width, None)

    def send_message(self, instance):
        user_msg = self.user_input.text.strip()
        if user_msg:
            self.add_chat(f"你: {user_msg}")
            bot_reply = self.get_bot_reply(user_msg)
            self.add_chat(f"朋友: {bot_reply}")
            self.user_input.text = ""

    def add_chat(self, message):
        timestamp = datetime.now().strftime('%H:%M')
        self.chat_history.text += f"[{timestamp}] {message}\n"

    def get_bot_reply(self, message):
        message = message.lower()
        
        greetings = ["你好", "嗨", "早安", "午安", "晚安"]
        sad_words = ["難過", "不開心", "傷心", "累"]
        happy_words = ["開心", "快樂", "太棒了"]
        question_words = ["你在幹嘛", "你是誰", "你會什麼"]
        
        if any(word in message for word in greetings):
            return random.choice([
                "嗨嗨！今天過得怎麼樣？",
                "哈囉～有什麼想跟我分享的嗎？",
                "嘿！我在這裡陪你～"
            ])
        elif any(word in message for word in sad_words):
            return random.choice([
                "你還好嗎？要不要跟我聊聊？",
                "如果想哭，就哭吧，我不會笑你。",
                "有時候難過是正常的，我會陪你。"
            ])
        elif any(word in message for word in happy_words):
            return random.choice([
                "哇～好替你開心！",
                "你的快樂也讓我覺得世界更美了！",
                "太好了！希望一直這麼開心～"
            ])
        elif any(word in message for word in question_words):
            return "我是一個喜歡聽你說話的小機器人啦～"
        elif "再見" in message:
            return "再見～如果想我，隨時可以打開我！"
        else:
            return random.choice([
                "嗯嗯，我聽著呢～",
                "這聽起來蠻有意思的，還有嗎？",
                "哇，說來聽聽更多嘛！",
                "我覺得你說得很好耶。"
            ])

class ChatApp(App):
    def build(self):
        return ChatBot()

if __name__ == "__main__":
    ChatApp().run()
