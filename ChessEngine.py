import numpy as np
 
"""
This file simulates a chess game. It checks the feasibility of given moves and reacts to different situations(for example when king's on check.)
"""

class ChessEngine:
    
    '''
    Constructor initializes the board in default standard with rows 1-8 and columns a-h.
    16 black pieces and 16 white pieces
    '''
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--",],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--",],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--",],
            ["--",  "--",  "--",  "--",  "--",  "--",  "--",  "--",],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.rows = ['1', '2', '3', '4', '5', '6', '7', '8']

        self.isWhite = True

        self.blackCheck = False
        self.whiteCheck = False

        self.moveLog = []

    
    def isPiece(row, column):
        return self.board[row][column] != "--"

    '''
    Checks all possible squares rook can move to. It is assumed that during this move actor player's king is not on check. 
    '''
    def rookMove(row, column):

        rook = self.board[row][column]
        
        # is rook white or black
        sign = rook[0]
        available_moves = []
        if rook[1] == 'R':
            
            # row+
            for i in range(row + 1, 9):
                trajectory = self.board[i][column]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[i] + this.column[column])

                    break

                available_moves.append(this.row[i] + this.column[column])
                
            # row-   
            for i in range(row - 1, 0, -1):
                trajectory = self.board[i][column]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[i] + this.column[column])

                    break

                available_moves.append(this.row[i] + this.column[column])

            # column+   
            for i in range(column + 1, 9):
                trajectory = self.board[row][i]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[row] + this.column[i])

                    break

                available_moves.append(this.row[row] + this.column[i])

            # column-  
            for i in range(column - 1, 0, -1):
                trajectory = self.board[row][i]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[row] + this.column[i])

                    break

                available_moves.append(this.row[row] + this.column[i])


        return available_moves

    """
     Checks all possible squares bishop can move to. It is assumed that during this time player king is not on check. 
    """
    def bishopMove(row, column):
        
        bishop = this.board[row][column]
        possible_moves = []

        if bishop[1] == 'B':
            # row+column+

            ppdistance = min(abs(row - 8), abs(column - 8))
            pfdistance = min(abs(row - 8), abs(column - 1))
            fpdistance = min(abs(row - 1), abs(column - 8))
            ffdistance = min(abs(row - 1), abs(column - 1))

            for i in range(1, ppdistance):
                
                trajectory = this.board[row + i][column + i]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[row] + this.column[i])

                    break

                available_moves.append(this.row[row] + this.column[i])                
                

            # row+column-
            for i in range(1, pfdistance):
                trajectory = this.board[row + i][column - i]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[row] + this.column[i])

                    break

                available_moves.append(this.row[row] + this.column[i])

            for i in range(1, fpdistance):
                trajectory = this.board[row - i][column + i]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[row] + this.column[i])

                    break

                available_moves.append(this.row[row] + this.column[i])  

            for i in range(1, ffdistance):
                trajectory = this.board[row - i][column - i]

                if trajectory != "--":

                    if trajectory[0] != sign:
                        available_moves.append(this.row[row] + this.column[i])

                    break

                available_moves.append(this.row[row] + this.column[i])  


        return possible_moves

        
    """
     Checks all possible squares king can move to. It is assumed that during this time player king is not on check. 
    """
    #def kingMove(row, column):
        
