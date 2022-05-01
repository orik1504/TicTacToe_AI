from asyncio.windows_events import INFINITE
from json.encoder import INFINITY
from board import  Gameboard
import numpy as np

def _minmax(board, depth = 1  ,is_maxsimaizer = True,):
    
    if board.is_endgame():
       return  get_value(board)

    if is_maxsimaizer:
        best_value = -np.inf
        for cell_combination in board.empty_cells():
            board.set_x(*cell_combination)
            best_value = max(best_value,_minmax(board ,depth+1, False)/depth)
            board.clear_cell(*cell_combination)
        return best_value       
    else:
        best_value = np.inf
        for cell_combination in board.empty_cells():
            board.set_o(*cell_combination)
            best_value = min(best_value,_minmax(board,depth+1 ,True)/depth)
            board.clear_cell(*cell_combination)
        return best_value
           
            

def minmax(board, ):
    best_combination = None
    best_value = -np.inf
    for cell_combination in board.empty_cells(): # * cell combination looks like this -> [row,col]
        board.set_x(*cell_combination)
        value = _minmax(board, is_maxsimaizer = False)
        if value>best_value:
            best_value = value
            best_combination = cell_combination
        board.clear_cell(*cell_combination)
    return best_combination

        

def get_value(baord):
    """ this function will return the value of certain path at the tree """
    if baord.is_o_win():
        return -10
    elif baord.is_x_win():
        return 10
    return 0

def copy_board(board,):
    checking_board = Gameboard(board._size)
    for row in range(board._size):
        for col in range(board._size):
            if board.is_x(row,col):
                checking_board.set_x(row,col)
            if board.is_o(row,col):
                checking_board.set_o(row,col)
    return checking_board


         

