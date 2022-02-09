class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def read_players():
    while True:
        first_player_name = input("First player name: ").strip()
        if first_player_name:
            break
    while True:
        second_player_name = input("Second player name: ").strip()
        if second_player_name != first_player_name and second_player_name:
            break
    while True:
        first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? ").upper()
        if first_player_sign in ['X', 'O']:
            break
    second_player_sign = 'X' if first_player_sign == 'O' else 'O'
    return Player(first_player_name, first_player_sign), Player(second_player_name, second_player_sign)


def print_num_state():
    print("""This is the numeration of the board:
|  1  |  2  |  3  |
|  4  |  5  |  6  |
|  7  |  8  |  9  |""")


def board_init_state(size_):
    board_ = []
    for row in range(size_):
        board_.append([None] * size)
    return board_


def print_current_board(board_):
    for row in board_:
        print('|  ', end='')
        print('  |  '.join([s if s else ' ' for s in row]), end='')
        print('  |')
    return board_


def is_valid_choice(board_,board_mapper_, choice):
    if choice < 1 or choice > 9:
        return False
    elif board_[board_mapper_[choice][0]][board_mapper_[choice][1]]:
        return False
    return True


def is_win_rows(board_):
    for row in board_:
        if len(set(row)) == 1 and set(row) != {None}:
            return True
    return False


def is_win_diagonals(board_, current_player_):
    diagonal_1, diagonal_2 = [], []
    for idx in range(len(board_)):
        diagonal_1.append(board_[idx][idx] == current_player_.sign)
        diagonal_2.append(board[idx][len(board_) - 1 - idx] == current_player_.sign)
    return all(diagonal_1) or all(diagonal_2)


def is_win_columns(board_, current_player_):
    for col in range(len(board_)):
        current_column = []
        for row in range(len(board_)):
            current_column.append(board_[row][col] == current_player_.sign)
        if all(current_column):
            return True
    return False


def is_draw(board_):
    for row_ in board_:
        if len([s for s in row_ if s]) < len(row_):
            return False
    return True


board_mapper = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                4: [1, 0], 5: [1, 1], 6: [1, 2],
                7: [2, 0], 8: [2, 1], 9: [2, 2]}

first_player, second_player = read_players()
size = 3
print_num_state()
print(f"{first_player.name} starts first!")

board = board_init_state(size)
turn = 1


while True:
    current_player = first_player if turn % 2 != 0 else second_player
    while True:
        current_choice = int(input(f'{current_player.name} choose a free position [1-9]: '))
        if is_valid_choice(board, board_mapper, current_choice):
            break
    row, col = board_mapper[current_choice]
    board[row][col] = current_player.sign
    print_current_board(board)
    if any([is_win_rows(board), is_win_columns(board, current_player), is_win_diagonals(board, current_player)]):
        print(f"{current_player.name} won!")
        break
    if is_draw(board):
        print('draw!')
        break
    turn += 1