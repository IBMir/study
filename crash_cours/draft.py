from classes import Die

cast = Die(20)
for i in range(6):
    print(cast.roll_die(), end= ' ')
