# функции НПЦ
import items
import mainchar

class NPC:
    name=str
    q=0 #количество обращений к нпц

    def __init__(self,name):
        self.name=name

class Merchant(NPC):
    greet = "Здарова я тарговец пакупай чтото или идинафиг"

    def sell(self, Character):
        pass

class People(NPC):
    camp = str
