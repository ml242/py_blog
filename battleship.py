board = []

def create_board():
    for i in range(0,5):
        board.append(["O"] * 5)
    return board

create_board()