
from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=100,size_hint_y=None,height=125,text="")
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello Lavde !",font_size=100)
        t.bind(text=l.setter('text'))
        f.add_widget(s)
        s.add_widget(l)
        b.add_widget(t)
        b.add_widget(f)
        return b

if __name__ == "__main__":
    TestApp().run()