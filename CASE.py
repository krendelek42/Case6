"""Case-study Тесселяция
Разработчики:
Докукина К.А., Назирова Е.С.

"""
import turtle as t

def get_numhexagons():

    num = int(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
    while True:
        try:
            if num >= 4 and num <= 20:
                return num
            else:
                num = int(input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: '))
        except ValueError:
            num = int(input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: '))


def get_color_choice():

    new_color = input('Пожалуйста, введите цвет: ').lower().strip()
    while True:
        if new_color == 'красный':
            choice = 'red'
            return choice
        if new_color == 'синий':
            choice = 'blue'
            return choice
        if new_color == 'зеленый':
            choice = 'green'
            return choice
        if new_color == 'желтый':
            choice = 'yellow'
            return choice
        if new_color == 'оранжевый':
            choice = 'orange'
            return choice
        if new_color == 'пурпурный':
            choice = 'purple'
            return choice
        if new_color == 'розовый':
            choice = 'pink'
            return choice
        else:
            new_color = input(
                    "'{}' не является верным значением. Пожалуйста, повторите попытку: ".format(new_color)).lower()


def draw_hexagon(x, y, side_len, color):

    t.pencolor('black')
    t.fillcolor(color)
    t.up()
    t.goto(x,y)
    t.right(30)
    t.begin_fill()
    t.down()
    for i in range(6):
        t.fd(side_len)
        t.right(60)
    t.end_fill()
    t.left(30)
    t.up()

