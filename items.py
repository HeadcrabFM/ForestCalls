import mainchar
# предметы, банки, оружие и тд

# банки
class item:
    name=str
    info=str
    cost = int
    bonus = int
    annotation = str

    def __init__(self, n,i,x, y):
        self.name=n
        self.info=i
        self.cost = x
        self.bonus = y

    def info(self):
        print(self.info)

class Drink(item):
    pass




class XPdrink(Drink):
    def use(self, Character):
        print(f'\nВыпито: {self.name}\nПолучено опыта: {self.bonus}')
        Character.xp += self.bonus
        Character.lvlup()
        Character.currentxp()

class Manadrink(Drink):
    def use(self, Character):
        Character.mana += self.bonus
        print(f'\nВыпито: {self.name}\nПолучено маны: {self.bonus}\nТекущий показатель маны: {Character.mana}')

class Moneydrink(Drink):
    def use(self, Character):
        Character.gold += self.bonus
        print("\nВыпито: Денежный напиток\nПолучено золота: ", self.bonus, '\nБаланс: ', Character.currentbalance())



pivas=XPdrink('Пивас','тмное пиво',300,7777)
ulun=Manadrink('Улун','чаёк :)', 420, 15)
