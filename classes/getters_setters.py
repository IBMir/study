class Point:
    '''Класс для представления координат точек на плоскости'''

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        return isinstance(x, int) or isinstance(x, float)

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числами.')

    def getCoords(self):
        return self.__x, self.__y


pt = Point(1, 2)
print(pt.getCoords())
pt.setCoords(5, 6)
print(pt.getCoords())
print(pt.__dict__)
pt._Point__x = 45
print(pt.__dict__)