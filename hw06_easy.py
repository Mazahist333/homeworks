# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class sped(object):

    def __init__(self, a, b, c, p):
        self.a = a
        self.b = b
        self.c = c
        self.p = p

    def S(self):
        self.c = (self.a * self.b) / 2
        print (self.c)

    def P(self):
        self.p = (self.a + self.b + self.c) * 2

        print(self.p)

    def H(self):
        print (u"Т.К треугольник прямоугольный, то H =", self.b)

P = sped(3, 2, 4, 3)

P.H()
P.S()
P.P()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Teapeze:

    def __init__(self,x ,y ,z, i, p, s, h, m, xz, yi):
                                               #     x ------- z
        self.x = x                             #    /|          \
        self.x = x                             #   /-|----m------\
        self.y = y                             #  /  |            \
        self.z = z                             # y __|h___________ i
        self.i = i
        self.h = h #высота
        self.p = p #периметр
        self.s = s #площадь
        self.m = m #средняя линия
        self.xz = xz
        self.yi = yi

    def check(self):
        if self.x * self.y == self.z * self.i:
            print("Проверка прошла успешно - Трапеция равнобочна")
        else:
            print("Трапеция не прошла проверку :(")

    def perimeter(self):
        self.p = self.x + self.y + self.z + self.i
        print(self.p)

    def square(self):
        self.s = 0.5 * self.h *(self.a + self.b)
        print(self.s)

    def sideXZ(self):
        self.xz = 2 * self.m - self.yi
        print(self.xz)

    def sideYI(self):
        self.yi = 2 * self.m -self.xz
        print(self.yi)


    #Не смог найти другие форумлы, т.к. все остальное через синусы и углы, а это
    # очень муторно. Простите  (μ_μ)