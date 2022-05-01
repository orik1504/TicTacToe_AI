"""
 x | x | x |
---+---+---+---
 x | x | x |
---+---+---
 x | x | x

"""
class Cell:

    def __init__(self):
        self.__value = 0
    
    def set_x(self):
        self.__value = 1
    
    def set_o(self):
        self.__value = 2

    def is_x(self):
        return self.__value == 1
    
    def is_o(self):
        return self.__value == 2
    
    def is_empty(self):
        return self.__value == 0
    
    def __str__(self):
        if self.is_x():
            return "x"
        
        if self.is_o():
            return "o"
        
        return " " 
    
    def clear(self):
        self.__value = 0
    
class Board:
    
    def __init__(self,board_size):
        self._size = board_size
        self._board = list()
        for _ in range(board_size):
            self._board.append([Cell() for _ in range(board_size)])
        
    def __str__(self):
        lines = list()
        for line in self._board:
            cur = ' ' + ' | '.join(str(cell) for cell in line) +'\n'
            lines.append(cur)
        
        sep =  "+".join("---" for _ in range(self._size))+"\n"

        return sep.join(lines)
    
    def set_x(self,row,col):
        if self.is_empty(row,col):
            self._board[row][col].set_x()
    
    def set_o(self,row,col):
        if self.is_empty(row,col):
            self._board[row][col].set_o()
    
    def is_x(self,row,col):
        return self._board[row][col].is_x()
    
    def is_o(self,row,col):
        return self._board[row][col].is_o()

    def is_empty(self,row,col):
        return self._board[row][col].is_empty()
    
    def empty_cells(self) -> list:
        ''' will return list of empty cells represented by thier [row,col] comination '''
        empty_cells = []
        for row in range(self._size):
            for col in range(self._size):
                if self.is_empty(row,col):
                    empty_cells.append([row,col])
        return empty_cells

    

    

class Gameboard(Board):
    
    def __row_x(self,row) -> list:
        return [cell.is_x() for cell in self._board[row]]
    
    def __row_o(self,row) -> list:
        return [cell.is_o() for cell in self._board[row]]

    def __col_x(self,col) -> list:
        col_list = []
        for row in range(self._size):
            col_list.append(self._board[row][col].is_x())
        return col_list
    
    def __col_o(self,col) -> list:
        col_o_list = []
        for row in range(self._size):
            col_o_list.append(self._board[row][col].is_o())
        return col_o_list
    
    def __diagonal_left_to_right_x(self) -> list:
        diagonal_x_list = []
        for index in range(self._size):
               diagonal_x_list.append(self._board[index][index].is_x())
        return diagonal_x_list
    
    def __diagonal_left_to_right_o(self) -> list:
        diagonal_o_list = []
        for index in range(self._size):
               diagonal_o_list.append(self._board[index][index].is_o())
        return diagonal_o_list

    def __diagonal_right_to_left_x(self) -> list:
        diagonal_x_list = []
        row = self._size -1
        for col in range(self._size):
            diagonal_x_list.append(self._board[row][col].is_x())
            row = row-1
        return diagonal_x_list
    
    def __diagonal_right_to_left_o(self) -> list:
        diagonal_o_list = []
        row = self._size-1
        for col in range(self._size):
            diagonal_o_list.append(self._board[row][col].is_o())
            row = row-1
        return diagonal_o_list
    
    def __is_x_row_win(self):
        for row in range(self._size):
            if len(set(self.__row_x(row))) == 1 and self.__row_x(row)[0] == True:
                return True
        return False
    
    def __is_o_row_win(self):
        for row in range(self._size):
            if len(set(self.__row_o(row))) == 1 and self.__row_o(row)[0] == True:
                return True
        return False
    
    def __is_x_col_win(self):
        for col in range(self._size):
            if len(set(self.__col_x(col))) == 1 and self.__col_x(col)[0] == True:
                return True
        return False
    
    def __is_o_col_win(self):
        for col in range(self._size):
            if len(set(self.__col_o(col))) == 1 and self.__col_o(col)[0] == True:
                return True
        return False

    def __is_x_diag_win(self):
        return len(set(self.__diagonal_left_to_right_x())) == 1 and self.__diagonal_left_to_right_x()[0] == True or len(set(self.__diagonal_right_to_left_x())) == 1 and self.__diagonal_right_to_left_x()[0] == True
    
    def __is_o_diag_win(self):
        return len(set(self.__diagonal_left_to_right_o())) == 1 and self.__diagonal_left_to_right_o()[0] == True or len(set(self.__diagonal_right_to_left_o())) == 1 and self.__diagonal_right_to_left_o()[0] == True
    
    def is_x_win(self):
        return self.__is_x_row_win() or self.__is_x_col_win() or self.__is_x_diag_win()
    
    def is_o_win(self):
        return self.__is_o_row_win() or self.__is_o_col_win() or self.__is_o_diag_win()

    def __is_win(self):
        return self.is_x_win() or self.is_o_win()
    
    def  __is_one_empty(self):
        is_empty = False
        for row in range(self._size):
            for col in range(self._size):
                if not is_empty == True:
                    is_empty = self.is_empty(row,col)
        return is_empty

    def is_draw(self):
        return not self.__is_win() and not self.__is_one_empty()
    
    def is_endgame(self) -> bool : 
        return self.is_draw() or self.is_o_win() or self.is_x_win()
    
    def clear_cell(self, row,col):
        self._board[row][col].clear()

                    


 
        
    
    
        

