#-------TIC TAC TOE-------#
        #---BOARD---#
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):

    print("\nBoard rules\n1 2 3\n4 5 6\n7 8 9\n\n")

    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+--+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

