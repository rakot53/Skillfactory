field = [['-']*3 for i in range(3)]


def greet():
    print("-------------------")
    print("  Приветствуем вас ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print(" По традиции первым\n  ходит крестик ")


def showField(f, us):
        print()
        print("    | 0 | 1 | 2 | ")
        print("  --------------- ")
        for i, row in enumerate(f):
            row_str = f"  {i} | {' | '.join(row)} | "
            print(row_str)
            print("  --------------- ")
        print(f"ходит - {us}")
        print()


def users_input(f):
    while True:
        place = input("Введите координаты: ").split()
        if len(place) != 2:
            print("Введите две координаты через пробел")
            continue

        if not (place[0].isdigit() and place[1].isdigit()):
            print("Вводите цифры")
            continue

        x, y = map(int, place)

        if x>=3 or x<0 or y>=3 or y<0:
            print("Вводите числа в диапазоне 0 до 2")
            continue

        if f[x][y] != '-':
            print("Клетка занята")
            continue
        break
    return x, y


def win(f, us):
    f_list = []
    for i in f:
        f_list += i
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    index = set([i for i, j in enumerate(f_list) if j == us])

    for p in positions:
        if len(index.intersection(set(p))) == 3:
            return True
    return False


greet()
count = 0
while True:
    if count % 2 == 0:
        user = 'x'
    else:
        user = 'o'

    showField(field, user)
    x, y = users_input(field)
    field[x][y] = user
    if count >= 4:
        if win(field, user):
            showField(field)
            print(f"{user} выйграл, начните заново")
            break

    if count == 8:
        showField(field)
        print("Ничья")
        break
    count += 1








