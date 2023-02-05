playing_field = [
    [0, 1, 2, 3],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
    [3, '-', '-', '-']
]
print("Приветствую тебя в игре \"КРЕСТИКИ НОЛИКИ\"\n")
player_X = input("Введите имя игрока, играющего крестиками: ")
player_O = input("Введите имя игрока, играющего ноликами: ")


def win(mark):
    for i in playing_field:
        if i.count(mark) > 2:
            return True
    if playing_field[1][1] == playing_field[2][1] == playing_field[3][1] == mark:
        return True
    if playing_field[1][2] == playing_field[2][2] == playing_field[3][2] == mark:
        return True
    if playing_field[1][3] == playing_field[2][3] == playing_field[3][3] == mark:
        return True
    if playing_field[1][1] == playing_field[2][2] == playing_field[3][3] == mark:
        return True
    if playing_field[1][3] == playing_field[2][2] == playing_field[3][1] == mark:
        return True


def print_field():
    print("Текущее игровое поле:")
    for i in range(4):
        for j in range(4):
            print(playing_field[i][j], end=' ')
        print()
    print()


def player_step(player):
    x, y = list(map(int, input(f"{player}, введите строку и столбец через пробел: ").split()))
    print(f"{player} ходит на {x} {y}")
    global playing_field
    playing_field[y][x] = "X" if player is player_X else "O"
    print_field()


print_field()
while True:
    player_step(player_X)
    if win("X"):
        print(f"Победа игрока {player_X}")
        break
    player_step(player_O)
    if win("O"):
        print(f"Победа игрока {player_O}")
        break
