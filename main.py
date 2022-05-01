from copy import copy
from posixpath import split
from board import  *
from minmax import minmax, copy_board



game_board = Gameboard(3)


while True:
     
     row,col = input("Where you want to put and 'o' ? (write {row},{col}) ").split(",")
     game_board.set_o(int(row),int(col))
     print(game_board)
     if game_board.is_endgame():
          print("o won")
          break
     checking_board = copy_board(game_board)
     combination = minmax(checking_board)
     game_board.set_x(combination[0],combination[1])
     print(game_board)
     if game_board.is_endgame():
          print("x won")
          break
     



