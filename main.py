import colorama


def create_chessboard():
    chessboard = ""
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                # Unicode white square
                chessboard += colorama.Back.WHITE + " "
            else:
                # Unicode black square
                chessboard += colorama.Back.BLACK + " "
        chessboard += "\n"
    return chessboard


def add_pieces(chessboard):
    # Unicode chess piece codes
    pieces = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    pawn = "♟"

    # Add black pieces to the chessboard
    chessboard = chessboard.replace(colorama.Back.BLACK + " ", colorama.Back.BLACK + pieces[0], 8)
    chessboard = chessboard.replace(colorama.Back.BLACK + "  ", colorama.Back.BLACK + pawn, 8)

    # Add white pieces to the chessboard
    chessboard = chessboard.replace(colorama.Back.WHITE + " ", colorama.Back.WHITE + pieces[0].lower(), 8 * 5)
    chessboard = chessboard.replace(colorama.Back.WHITE + "  ", colorama.Back.WHITE + pawn.lower(), 8)

    return chessboard


# Initialize colorama
colorama.init()

# Create an empty chessboard
board = create_chessboard()

# Add chess pieces to the board
board_with_pieces = add_pieces(board)

# Print the chessboard with pieces
print(board_with_pieces)

# Reset colorama settings
colorama.deinit()