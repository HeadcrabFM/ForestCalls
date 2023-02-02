import mainchar


class Forest:
    name = str

    def __init__(self, x):
        self.name = x

    def gowild(self):
        mainchar.protagonist.currentcamp = self.name
        print('\nВЫ НАХОДИТЕСЬ В ЛЕСУ.')
        mainchar.protagonist.charstate()
        mainchar.protagonist.goto()


class Places(Forest):  # сабкласс для описывания саблок в лесу
    pass


class Camp:
    name = str
    naselenie = int
    reputation = int
    quest = int  # колво квестов

    def __init__(self, x, y):
        self.name = x
        self.naselenie = y

    def entry(self):
        mainchar.protagonist.currentcamp = self.name
        print(f'\nВЫ НАХОДИТЕСЬ В ЛАГЕРЕ {self.name}')
        mainchar.protagonist.charstate()
        a = int(input(f'\nНажмите 1 чтобы оглядеться, 2 чтобы выйти из лагеря:\n>>> '))
        if a == 1:
            self.lookaround()
        elif a == 2:
            mainchar.protagonist.goto()
        else:
            print('Выберите п.1 или п.2')

    def lookaround(self):
        a = int(input(f'\nВыбрите 1 для костра, 2 для выхода из лагеря {self.name}\n>>> '))
        if a == 1:
            self.campfire()
        elif a == 2:
            mainchar.protagonist.goto()
        else:
            input('Введите 1 или 2: ')

    def campfire(self):
        print('Вы у костра но сделать пока ниче нельзя. Нажмите Энтер...')
        input()
        mainchar.protagonist.goto()


# создаю все 4 локации:
Forest = Forest('ДРЕВНИЙ ЛЕС')
Vishenka = Camp('ВИШЕНКА', 9)
LonelyPine = Camp('ОДИНОКАЯ СОСНА', 13)
PikPnya = Camp('ПИК ПНЯ', 5)
