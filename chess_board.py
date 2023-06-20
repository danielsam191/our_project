# array = [[rook_black, knight_black, bishop_black, queen_black, king_black, bishop_black, knight_black, rook_black],
#          [pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black],
#          [pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white],
#          [rook_white, knight_white, bishop_white, queen_white, king_white, bishop_white, knight_white,rook_white]]


from colorama import Back, Style, Fore
def create_chess_board():
    chess_board = []
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                chess_board.append(Back.WHITE + "     ")
            else:
                chess_board.append(Back.BLACK + "     ")
        chess_board.append(Back.RESET + " ")
        chess_board.append("\n")
    return chess_board
def print_board(chess_board):
    print("".join(chess_board))

def add_pices_start(chess_board):
    king_black, king_white = chr(0x2654), chr(0x265A)
    queen_black, queen_white = chr(0x2655), chr(0x265B)
    rook_black, rook_white = chr(0x2656), chr(0x265C)
    knight_black, knight_white = chr(0x2658), chr(0x265E)
    pawn_black, pawn_white = chr(0x2659), chr(0x265F)
    bishop_black, bishop_white = chr(0x2657), chr(0x265D)
    # WHITE ARMY
    chess_board[0] = Back.WHITE + '  '+ "R" + "  "
    chess_board[1] = Back.BLACK + '  '+ "H" + "  "
    chess_board[2] = Back.WHITE + '  '+ "B" + "  "
    chess_board[3] = Back.BLACK + '  '+ "Q" + "  "
    chess_board[4] = Back.WHITE + '  '+ "K" + "  "
    chess_board[5] = Back.BLACK + '  '+ "B" + "  "
    chess_board[6] = Back.WHITE + '  '+ "H" + "  "
    chess_board[7] = Back.BLACK + '  '+ "R" + "  "
    chess_board[10] = Back.BLACK + '  '+ "P" + "  "
    chess_board[11] = Back.WHITE + '  ' + "P" + "  "
    chess_board[12] = Back.BLACK + '  ' + "P" + "  "
    chess_board[13] = Back.WHITE + '  ' + "P" + "  "
    chess_board[14] = Back.BLACK + '  ' + "P" + "  "
    chess_board[15] = Back.WHITE + '  ' + "P" + "  "
    chess_board[16] = Back.BLACK + '  ' + "P" + "  "
    chess_board[17] = Back.WHITE + '  ' + "P" + "  "
    #BLACK ARMY
    chess_board[-3] = Back.WHITE + '  '+ "r" + "  "
    chess_board[-4] = Back.BLACK + '  '+ "b" + "  "
    chess_board[-5] = Back.WHITE + '  '+ "h" + "  "
    chess_board[-6] = Back.BLACK + '  '+ "k" + "  "
    chess_board[-7] = Back.WHITE + '  '+ "q" + "  "
    chess_board[-8] = Back.BLACK + '  '+ "r" + "  "
    chess_board[-9] = Back.WHITE + '  ' + "b" + "  "
    chess_board[-10] = Back.BLACK + '  '+ "r" + "  "
    chess_board[-13] = Back.BLACK + '  '+ "p" + "  "
    chess_board[-14] = Back.WHITE + '  ' + "p" + "  "
    chess_board[-15] = Back.BLACK + '  ' + "p" + "  "
    chess_board[-16] = Back.WHITE + '  ' + "p" + "  "
    chess_board[-17] = Back.BLACK + '  ' + "p" + "  "
    chess_board[-18] = Back.WHITE + '  ' + "p" + "  "
    chess_board[-19] = Back.BLACK + '  ' + "p" + "  "
    chess_board[-20] = Back.WHITE + '  ' + "p" + "  "
    chess_board


    return chess_board

    return chess_board

a = create_chess_board()
a = add_pices_start(a)
print_board(a)