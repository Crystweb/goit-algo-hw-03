# Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, використовуючи стрижень В як допоміжний.
# Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.

def hanoi(n, source, auxiliary, target, state):
    if n == 1:
        move_disk(source, target, state)
    else:
        hanoi(n - 1, source, target, auxiliary, state)
        move_disk(source, target, state)
        hanoi(n - 1, auxiliary, source, target, state)


def move_disk(source, target, state):
    disk = state[source].pop()
    state[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")


def main(n):
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")


if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    main(n)
