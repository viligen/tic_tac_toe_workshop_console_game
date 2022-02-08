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


first_player, second_player = read_players()
size = 3
print_num_state()
print(f"{first_player.name} starts first!")
