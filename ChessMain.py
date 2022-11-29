import pygame as p
import ChessEngine

"""
This file is responsible for displaying the current situation of the game
"""

# Dimensions
HEIGHT = 600
WIDTH = 512
HEIGHT512 = 512
DIMENSION = 8 # 8x8 board
SQUARE_SIZE = HEIGHT512 // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for elem in pieces:
        IMAGES[elem] = p.transform.scale(p.image.load("images/" + elem +".png"), (SQUARE_SIZE, SQUARE_SIZE))



def main():
    p.init()
    screen = p.display.set_mode([WIDTH, HEIGHT], vsync=1)
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.ChessEngine()
    validMoves = gs.getValidMoves()
    moveMade = True
    loadImages()
    running = True
    squareSelected =  () # keeps track of the last mouse click
    playerClicks = [] # keeps track of player clicks
    while running:
        
        # pygame.event().get() checks if user gave an input.
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x, y)
                column = location[0]//SQUARE_SIZE
                row = location[1]//SQUARE_SIZE    
                if squareSelected == (row, column):
                    squareSelected = () # deselect
                    playerClicks = [] # clears the player clicks
                else:
                    squareSelected = (row, column)
                    playerClicks.append(squareSelected)
                if len(playerClicks) == 2: # after second click
                    # first click signfies the piece that'll be moved, the second click is its destination.
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board) 
                    print(move.getChessNotation()) # prints the moved piece.
                    if move in validMoves:
                        gs.makeMove(move) # making the move
                        moveMade = True
                    squareSelected = () # resets user clicks
                    playerClicks = [] 
            # key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # undo when "z" is pressed
                    gs.undoMove()
                    moveMade = True
                
        
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False   
        
        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, gs)
        
        
        

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

"""Draws 8x8 chess board."""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(r*SQUARE_SIZE, c*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  


"""Set all the pieces in default chess position."""
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            elem = board[row][column]
            if elem != "--":
                # Blit draws image on the board
                screen.blit(IMAGES[elem], p.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Code will only run when executed from this file.
if __name__ == '__main__':
    main()
