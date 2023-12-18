import chess
import chess.svg
import chess.engine

def main():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        legal_moves = [move.uci() for move in board.legal_moves]
        print("Legal moves:", legal_moves)

        move = input("Enter your move (in UCI format, e.g., 'e2e4'): ")
        if move in legal_moves:
            board.push_uci(move)
        else:
            print("Invalid move. Try again.")

    print("Game Over")
    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    elif board.is_insufficient_material():
        print("Insufficient material to checkmate.")
    elif board.is_seventyfive_moves():
        print("The game ended in a draw due to the seventy-five moves rule.")
    elif board.is_fivefold_repetition():
        print("The game ended in a draw due to fivefold repetition.")
    elif board.is_variant_draw():
        print("The game ended in a draw due to a specific variant rule.")
    else:
        print("Game result: " + board.result())

if __name__ == "__main__":
    main()
