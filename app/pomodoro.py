from itertools import cycle
from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty , BooleanProperty

class Cycle:
    def __init__(self):
        self.cycle = cycle [
            Timer(25),Timer(5),
            Timer(25),Timer(5),
            Timer(25),Timer(30)]

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cycle)


class Timer:
    def __init__(self,time):
        self.time = time * 60

    def decrementar(self):
        self.time -= 1
        return self.time

    def __str__(self):
        return"{:02d}:{:02d}".format(*divmod(self.time,60))

class Pomodoro(MDFloatLayout):
    timer_str=StringProperty("25:00")
    button_str =StringProperty("Pausar!")
    runnning = BooleanProperty(False)
    #cycle = Cycle()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #self._time = next(self.cycle)
        


    def start(self):
        self.button_str = "Pausar!"

        if self.runnning:
            self.runnning = False
    
    def stop(self):
        self.button_str = "Reiniciar!"
        if not self.runnning:
            self.runnning = True

    def click(self):
        
        if self.runnning:
            self.start()
        else:
            self.stop()



class Promodoro(MDApp):

    

    def build_app(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = '700'
        return Builder.load_file("app/pomodoro.kv")
    
