import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import webbrowser

# App Background Color (Dark Navy Blue)
Window.clearcolor = (0.02, 0.02, 0.08, 1)

# 1. පටන් ගන්නා විට පෙන්වන බලගතු Credit සහතිකය
class CreditSplashScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Title
        layout.add_widget(Label(text="NOVA MEGA AI HUB", font_size='35sp', bold=True, color=(0, 1, 0.8, 1)))
        
        # Certificate Box
        cert_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        cert_layout.add_widget(Label(text="--- OFFICIAL OWNERSHIP CERTIFICATE ---", font_size='14sp', color=(1, 1, 1, 0.5)))
        
        # Owner Info
        cert_layout.add_widget(Label(text="LEGAL OWNER: CHAMOD", font_size='28sp', bold=True, color=(1, 0.84, 0, 1)))
        cert_layout.add_widget(Label(text="LICENSE KEY: CH-990-NOVA-2025", font_size='14sp', color=(0.5, 0.8, 1, 1)))
        cert_layout.add_widget(Label(text="SECURITY STATUS: VERIFIED & ENCRYPTED", font_size='12sp', color=(0, 1, 0, 0.8)))
        
        layout.add_widget(cert_layout)
        
        layout.add_widget(Label(text="This software is protected under global AI rights.\nUnauthorized distribution is prohibited.", 
                                halign='center', font_size='12sp', color=(1, 1, 1, 0.4)))
        
        # Continue Button
        btn_continue = Button(text="ACCEPT & CONTINUE", size_hint=(1, 0.15), 
                               background_color=(0, 0.6, 1, 1), background_normal='', bold=True)
        btn_continue.bind(on_press=self.go_next)
        layout.add_widget(btn_continue)
        
        self.add_widget(layout)

    def go_next(self, instance):
        self.manager.current = 'language'

class LanguageScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text="SELECT LANGUAGE", font_size='24sp', bold=True))
        btn = Button(text="ENGLISH / සිංහල", size_hint=(1, 0.2), background_color=(0.4, 0.1, 0.8, 1), background_normal='')
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'register'))
        layout.add_widget(btn)
        self.add_widget(layout)

class RegisterScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text="USER VERIFICATION", font_size='22sp'))
        self.name_input = TextInput(hint_text="Enter Your Name...", multiline=False, size_hint=(1, 0.2), font_size='18sp')
        layout.add_widget(self.name_input)
        
        btn = Button(text="VERIFY IDENTITY", size_hint=(1, 0.2), background_color=(0, 0.7, 0.9, 1), background_normal='')
        btn.bind(on_press=self.verify_user)
        layout.add_widget(btn)
        self.add_widget(layout)

    def verify_user(self, instance):
        input_name = self.name_input.text.strip()
        if input_name:
            if input_name.lower() == "chamod":
                status = "MASTER OWNER (CERTIFIED)"
                msg_color = (1, 0.84, 0, 1)
            else:
                status = "VERIFIED USER"
                msg_color = (1, 1, 1, 1)

            content = BoxLayout(orientation='vertical', padding=20)
            content.add_widget(Label(text=f"User: {input_name}\nStatus: {status}", halign='center', color=msg_color))
            self.popup = Popup(title='System Verification', content=content, size_hint=(0.8, 0.4))
            self.popup.open()
            self.manager.get_screen('main').update_ui(input_name, status, msg_color)
            Clock.schedule_once(self.go_main, 2)

    def go_main(self, dt):
        self.popup.dismiss()
        self.manager.current = 'main'

class MainHub(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        self.owner_label = Label(text="NOVA MEGA HUB", size_hint=(1, 0.1), font_size='20sp', bold=True)
        layout.add_widget(self.owner_label)

        layout.add_widget(Label(text="ASK ANYTHING (AI):", size_hint=(1, 0.05)))
        self.ai_input = TextInput(hint_text="Ask any question...", size_hint=(1, 0.12))
        layout.add_widget(self.ai_input)

        layout.add_widget(Label(text="UNLIMITED SEARCH (18+ OK):", size_hint=(1, 0.05)))
        self.search_input = TextInput(hint_text="Search videos or sites...", size_hint=(1, 0.12))
        layout.add_widget(self.search_input)
        
        btn_search = Button(text="EXPLORE WITHOUT LIMITS", size_hint=(1, 0.15), background_color=(1, 0, 0.4, 1), bold=True, background_normal='')
        btn_search.bind(on_press=self.do_search)
        layout.add_widget(btn_search)
        self.add_widget(layout)

    def update_ui(self, name, status, color):
        self.owner_label.text = f"{name} - {status}"
        self.owner_label.color = color

    def do_search(self, instance):
        query = self.search_input.text
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")

class NovaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CreditSplashScreen(name='splash'))
        sm.add_widget(LanguageScreen(name='language'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(MainHub(name='main'))
        return sm

if _name_ == '_main_':
    NovaApp().run()
