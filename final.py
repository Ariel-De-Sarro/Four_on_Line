
def draw_field(field):
    for row in range(11):
        if row % 2 == 0:
            new_row = int(row/2)
            for column in range(13):
                if column % 2 == 0:
                    new_column = int(column/2)
                    if column != 12:
                        print(field[new_row][new_column], end='')
                    else:
                        print(field[new_row][new_column])
                else:
                    print('|', end='')
        else:
            print('-------------')


Player_1 = input('Player 1: Ingrese su nombre\n')
Player_2 = input('Player 2: Ingrese su nombre\n')
players = {Player_1: 'X', Player_2: 'O'}


def check_winner(board):
    board_height = len(board)
    board_width = len(board[0])
    global Game_Over

    for key in players:
        for i in range(board_height):
            for j in range(board_width - 3):
                if board[i][j] == players[key] and board[i][j+1] == players[key] and board[i][j+2] == players[key] \
                        and board[i][j+3] == players[key]:
                    print(f'{key} is the winner!!!')
                    Game_Over = True

        for j in range(board_width):
            for i in range(board_height - 3):
                if board[i][j] == players[key] and board[i+1][j] == players[key] and board[i+2][j] == players[key] \
                        and board[i+3][j] == players[key]:
                    print(f'{key} is the winner!!!')
                    Game_Over = True

        for j in range(board_width - 3):
            for i in range(board_height - 3):
                if board[i][j] == players[key] and board[i+1][j+1] == players[key] and board[i+2][j+2] == players[key] \
                        and board[i+3][j+3] == players[key]:
                    print(f'{key} is the winner!!!')
                    Game_Over = True
                elif board[i][j] == players[key] and board[i-1][j-1] == players[key] and \
                        board[i-2][j-2] == players[key] and board[i-3][j-3] == players[key]:
                    print(f'{key} is the winner!!!')
                    Game_Over = True
                elif board[i][j] == players[key] and board[i+1][j-1] == players[key] and \
                        board[i+2][j-2] == players[key] and board[i+3][j-3] == players[key]:
                    print(f'{key} is the winner!!!')
                    Game_Over = True
                elif board[i][j] == players[key] and board[i-1][j+1] == players[key] and \
                        board[i-2][j+2] == players[key] and board[i-3][j+3] == players[key]:
                    print(key, ' is the winner!!!')
                    Game_Over = True


currentField = [[' ' for i in range(7)] for x in range(6)]
draw_field(currentField)

Game_Over = False
Player = 1


while not Game_Over:
    print('Players turn:', Player)
    MoveColumn = int(input('Please enter the column: \n'))
    if Player == 1:
        if currentField[5][MoveColumn] == ' ':
            currentField[5][MoveColumn] = 'X'
            Player = 2
        elif currentField[4][MoveColumn] == ' ':
            currentField[4][MoveColumn] = 'X'
            Player = 2
        elif currentField[3][MoveColumn] == ' ':
            currentField[3][MoveColumn] = 'X'
            Player = 2
        elif currentField[2][MoveColumn] == ' ':
            currentField[2][MoveColumn] = 'X'
            Player = 2
        elif currentField[1][MoveColumn] == ' ':
            currentField[1][MoveColumn] = 'X'
            Player = 2
        elif currentField[0][MoveColumn] == ' ':
            currentField[0][MoveColumn] = 'X'
            Player = 2
    else:
        if currentField[5][MoveColumn] == ' ':
            currentField[5][MoveColumn] = 'O'
            Player = 1
        elif currentField[4][MoveColumn] == ' ':
            currentField[4][MoveColumn] = 'O'
            Player = 1
        elif currentField[3][MoveColumn] == ' ':
            currentField[3][MoveColumn] = 'O'
            Player = 1
        elif currentField[2][MoveColumn] == ' ':
            currentField[2][MoveColumn] = 'O'
            Player = 1
        elif currentField[1][MoveColumn] == ' ':
            currentField[1][MoveColumn] = 'O'
            Player = 1
        elif currentField[0][MoveColumn] == ' ':
            currentField[0][MoveColumn] = '0'
            Player = 1
    draw_field(currentField)
    check_winner(currentField)
