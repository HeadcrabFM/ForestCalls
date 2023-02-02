# Скрипт для описания класса главного персонажа
import location

class Character:
    name = str
    age = int
    lvl = int
    xp = int
    gold = int
    hp = int
    maxhp = int
    mana = int
    maxmana = int
    currentcamp = str

    guild = None
    camp = None

    type = str

    # массив со списком всех значений для вывода
   # sp = [['ИМЯ:',name],['Возраст:',age],['Уровень:',lvl],['Опыт:',xp],['Деньги:',gold],['Здоровье:',hp],['Макс.здоровье:',maxhp],['Мана:',mana],['Макс.мана:',maxmana],['\nТекущий лагерь:',currentcamp],['\nГильдия:',guild],['Родной лагерь:',camp]]

    def __init__(self, x, y):
        self.name = x
        self.age = y
        self.lvl = 1
        self.xp = 0
        self.gold = 1000
        self.mana = 100
        self.maxmana = 100
        self.hp = 100
        self.maxhp = 100

    def lvlup(self):
        if self.xp >= 100:
            self.lvl += self.xp // 100
            self.maxhp += (self.xp // 100) * 5
            self.maxmana += (self.xp // 100) * 5
            self.xp %= 100
            print("Новый уровень! ", self.lvl)

    def currentxp(self):
        print('Текущий опыт: ', self.xp)
        print('До след. уровня: ', 100 - self.xp)

    def currentlvl(self):
        return self.lvl

    def getgold(self, x):
        self.gold += x
        print(Character.name, "получает деньги: +", x)

    def currentbalance(self):
        return self.gold

    def charstate(self):
        print('\nСтатус:', self.__dict__)

   #пытаюсь вывести красивую таблу
    def charstatediff(self):
        for i in range(12):
            for j in range(2):
                print (self.sp[i][j])

    def currentcamp(self):
        return self.currentcamp()

    # Переход между локациями, надо пофиксить исключение
    def goto(self):
        a = int(input('\nКуда идти:\n1 - Лагерь Пик Пня\n2 - лагерь Одинокая Сосна\n3 - лагерь Вишенка\n4 - Лес\n>>> '))
        if (a == 1):
            location.PikPnya.entry()
        elif (a == 2):
            location.LonelyPine.entry()
        elif (a == 3):
            location.Vishenka.entry()
        elif (a == 4):
            location.Forest.gowild()
        else:
            print('\nВыбери вариант 1-4: ')


# инвентарь можно сделать как массив с переменными
# В объект мейн чара необходимо сохранять его текущий статус, т.е.:

# Содаём персонажа
def createchar():
    print('Создание нового главного персонажа')
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    prot = Character(name, age)
    print('Создан новый персонаж: ', prot.__dict__)
    return prot





class Stats:
    attack = int
    gather = int
    magic = int
    plus = int
    types = ['Воинственный', 'Собиратель', 'Упоротый']
    statlist=['attack']

    def __init__(self, Character, a):
        if (a == 1):
            self.attack = 3
            self.gather = 1
            self.magic = 1
            Character.type = self.types[a - 1]
        elif (a == 2):
            self.attack = 1
            self.gather = 3
            self.magic = 1
            Character.type = self.types[a - 1]
        elif (a == 3):
            self.attack = 1
            self.gather = 1
            self.magic = 3
            Character.type = self.types[a - 1]

    def statlayout(self):
        pass

    def Upstat(self, plus):
        self.a[1] += plus

# Объекты классов (надо ли оно?.. хз где создавать объекты класса)
protagonist = Character
protstats = Stats(protagonist,3)