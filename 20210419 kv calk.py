'''
Калькулятор
https://www.youtube.com/watch?v=Mu4mps4imJ4&t=53s
'''

import kivy
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class CalculatorApp(App):
    icon = 'free-icon-abacus-4525747.png'

    def update_label(self):
        self.root.ids.input.text = self.formula

    def update_label_clear(self, instance):
        self.formula = ''
        self.update_label()

    def add_number(self, instance):

        if instance.text != '=' and instance.text != 'C':
            self.formula += str(instance.text)
            self.update_label()

        if instance.text == '=':
            try:
                self.formula = str(eval(self.formula))
                self.update_label()
                self.formula = ''
            except:
                self.formula = ''
                self.update_label()

    def build(self):
        self.title = "Calc_Yura"
        self.formula = ''
        # main window
        return NumButtonsLayout()


class NumButtonsLayout(BoxLayout):
    pass


if __name__ == '__main__':
    # Here the class MyApp is initialized
    # and its run() method called.
    CalculatorApp().run()
