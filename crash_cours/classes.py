from random import randint

class Military():
    '''Обычный военный'''

    def __init__(self, rank, last_name, position):
        self.rank = rank
        self.last_name = last_name
        self.position = position

    def greeting(self):
        '''Приветствие'''
        print(f'Здравия желаю товарищь {self.rank} {str(self.last_name).title()}.')

    def new_renk(self):
        '''Присвоение звания'''
        rk = ['лейтенант', 'старший лейтенант', 'капитан', 'майор', 'подполковник', 'полковник', 'генирал',
              'министр обороны', 'президент']
        print(
            f'Товарищь {self.rank} {str(self.last_name).title()}, за добросовестное исполнение обязанностей в должности {self.position},'
            f' вам присвоили очередное звание - {rk[rk.index(self.rank) + 1]}.')


class Soldier(Military):
    '''Обычный солдат'''

    def __init__(self, rank, last_name, position):
        super(Soldier, self).__init__(rank, last_name, position)
        self.toilet = 'туалет'

    def slave(self):
        print(f'{str(self.rank).title()} {str(self.last_name).title()}, бегом работать!!!')
    def toit(self):
        print(f'{str(self.position).title()}, бегом чистить {self.toilet}!!!')

class Die():
    '''Шестигранный кубик'''

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        '''Бросок кубика'''
        return randint(1, self.sides)

if __name__ == '__main__':
    cast = Die()
    print(cast.roll_die())