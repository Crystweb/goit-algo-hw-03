# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, що користувач
# повинен мати можливість вказати рівень рекурсії.

import turtle
import argparse


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main(order):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість малювання

    # Положення
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    # Малювання сніжинки
    koch_snowflake(t, order, 300)
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Намалювати сніжинку Коха з заданим рівнем рекурсії.')
    parser.add_argument('order', type=int, help='Рівень рекурсії сніжинки')
    args = parser.parse_args()

    main(args.order)
