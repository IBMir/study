class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'{self.__x}, {self.__y}'

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width

class Line(Prop):
    def __init__(self, *args):
        print('Переопределенный конструкто класса Line')
        super().__init__(*args)

    def drawLine(self):
        print(f'Рисуем {self._sp}, {self._ep}, {self._color}, {self.getWidth()}.')

class Rect(Prop):
    def drawLine(self):
        print(f'Рисуем {self._sp}, {self._ep}, {self._color}, {self.getWidth}.')


l = Line(Point(), Point(1, 2))
print(l.__dict__)
l.drawLine()