# Define an empty chess board
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Print the chess board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Main game loop
player = 1  # Player 1 starts
while True:
    print_board(board)
    move = input(f'Player {player}, enter your move (e.g., e2 to e4): ')
    if move == 'quit':
        print('Game Over. Quitting.')
        break
    if len(move) != 4:
        print('Invalid move. Try again.')
        continue

    from_col, from_row, to_col, to_row = move[0], move[1], move[2], move[3]
    from_col, from_row, to_col, to_row = ord(from_col) - 97, int(from_row) - 1, ord(to_col) - 97, int(to_row) - 1

    piece = board[from_row][from_col]
    if piece == ' ':
        print('No piece to move. Try again.')
        continue

    board[to_row][to_col] = piece
    board[from_row][from_col] = ' '

    player = 3 - player  # Switch players (1 <-> 2)

print_board(board)
