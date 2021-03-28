"""Case-study Тесселяция
Разработчики:
Докукина К.А. 60%, Назирова Е.С. 40%

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

colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
print('Допустимые цвета заливки:')
for i in colors:
    print(' '+i)
color_1 = get_color_choice()
color_2 = get_color_choice()
num = get_numhexagons()
diameter = 1000/(2*num + 1)
side_len = diameter / (3**(0.5))
x = -250 + diameter/2
y = 250

t.setup(500,500)
t.speed(1000)
colors = [color_1, color_2]
index = 0
for i in range(num):
    for j in range(num):
        color_index = (index+j)%2
        draw_hexagon(x,y,side_len,colors[color_index])
        x += (-1)**(i%2)* diameter
    if i %2 == 0:
        index = color_index
    else:
        index = color_index + 1
    x += (-1) ** (i+1)*(diameter/2)
    y -= (3/2 * side_len)

t.mainloop()
