import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

kivy.require('1.9.0')
Config.set('graphics', 'resizable', 1)

class Calculatrice(GridLayout):
    def calculer(self, calcul):
        if calcul:
            try:
                self.display.text = str(eval(calcul))
            except Exception:
                self.display.text = "Erreur"
                self.display.background_color = "red"

    def clearError(self, value):
        if("Erreur" in self.display.text):
            self.display.text = value
            self.display.background_color = "white"

class MainWindow(App):
    def build(self):
        return Calculatrice()

window = MainWindow()
window.run()