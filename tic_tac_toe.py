a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
i = "i"
count = 0
field = f""" 
            Добро пожаловать в игру Крестики-Нолики!
        Ниже представлено импровизированное поле для игры:
                        _{a}_[_{b}_]_{c}_
                        _{d}_[_{e}_]_{f}_
                        _{g}_[_{h}_]_{i}_
    Для хода вам нужно указать адрес клетки и ход будет зачтен
        Как вы заметили, каждая клетка имеет свой адрес
                Первый ход начинает крестик (X)
                        Приятной игры :)
    """


def field_f():
    global field
    field = f""" 
            Добро пожаловать в игру Крестики-Нолики!
        Ниже представлено импровизированное поле для игры:
                        _{a}_[_{b}_]_{c}_
                        _{d}_[_{e}_]_{f}_
                        _{g}_[_{h}_]_{i}_
    Для хода вам нужно указать адрес клетки и ход будет зачтен
        Как вы заметили, каждая клетка имеет свой адрес
                Первый ход начинает крестик (X)
                        Приятной игры :)
    """
    print(field)


def x_turn(turn_x):
    global a, b, c, d, e, f, g, h, i, count
    if turn_x == "a" and a != "X" and a != "O":
        a = "X"
        return a
    elif turn_x == "b" and b != "X" and b != "O":
        b = "X"
        return b
    elif turn_x == "c" and c != "X" and c != "O":
        c = "X"
        return c
    elif turn_x == "d" and d != "X" and d != "O":
        d = "X"
        return d
    elif turn_x == "e" and e != "X" and e != "O":
        e = "X"
        return e
    elif turn_x == "f" and f != "X" and f != "O":
        f = "X"
        return f
    elif turn_x == "g" and g != "X" and g != "O":
        g = "X"
        return g
    elif turn_x == "h" and h != "X" and h != "O":
        h = "X"
        return h
    elif turn_x == "i" and i != "X" and i != "O":
        i = "X"
        return i
    else:
        print("Неверный ввод! Попробуйте снова!")
        count -= 1


def o_turn(turn_o):
    global a, b, c, d, e, f, g, h, i, count
    if turn_o == "a" and a != "X" and a != "O":
        a = "O"
        return a
    elif turn_o == "b" and b != "X" and b != "O":
        b = "O"
        return b
    elif turn_o == "c" and c != "X" and c != "O":
        c = "O"
        return c
    elif turn_o == "d" and d != "X" and d != "O":
        d = "O"
        return d
    elif turn_o == "e" and e != "X" and e != "O":
        e = "O"
        return e
    elif turn_o == "f" and f != "X" and f != "O":
        f = "O"
        return f
    elif turn_o == "g" and g != "X" and g != "O":
        g = "O"
        return g
    elif turn_o == "h" and h != "X" and h != "O":
        h = "O"
        return h
    elif turn_o == "i" and i != "X" and i != "O":
        i = "O"
        return i
    else:
        print("Неверный ввод! Попробуйте снова!")
        count -= 1


while True:
    field_f()
    count += 1
    if count % 2 != 0:
        turn = input("Ходите, X: ").lower()
        x_turn(turn)
    else:
        turn = input("Ходите, O: ").lower()
        o_turn(turn)
    if a == b == c:
        field_f()
        print(f"Выиграл {a}!")
        break
    elif d == e == f:
        field_f()
        print(f"Выиграл {d}!")
        break
    elif g == h == i:
        field_f()
        print(f"Выиграл {g}!")
        break
    elif a == d == g:
        field_f()
        print(f"Выиграл {a}!")
        break
    elif b == e == h:
        field_f()
        print(f"Выиграл {b}!")
        break
    elif c == f == i:
        field_f()
        print(f"Выиграл {c}!")
        break
    elif a == e == i:
        field_f()
        print(f"Выиграл {a}!")
        break
    elif g == e == c:
        field_f()
        print(f"Выиграл {g}!")
        break
    elif count >= 9:
        field_f()
        print("Ничья!")
        break
    else:
        continue
