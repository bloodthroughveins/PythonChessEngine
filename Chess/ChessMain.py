"""
The main driver file it will be responsible for handling the players user input and displaying the current gamestate obj
shout some random teacher on the internet who im learning this from thanks :)
"""
import pygame as p
from Chess import ChessEngine
p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8       # chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60        # for anim
IMAGES = {}

"""
Init a global dictionary of images only called once in main to preserve performance
"""
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ', ]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # We can access the image by saying draw this image by calling 'IMAGES['wp']'


"""
Main driver handles the users inputs and handles the updating/frames of graphics and updates them accordingly
hopefully adding drag and drop wont fuck with pygames renderer
"""
def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()    # this right here calls chess engine to load and create the board
    load_images()    # only do this once before the while loop
    running = True
    sqSelected = () #   no square is selected. keeps track of the last click a user clicked (row colum etc)
    playerClicks = []      # keeps track of players clicks in a list form
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()    # (x , y) of location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):    # player clcked the same square twice
                    sqSelected = ()     #   deselect
                    playerClicks = []   # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)     #append for both 1 and 2nd clicks
                if len(playerClicks) == 2:  #   after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()     # resets the players clicks if not will infinitely append
                    playerClicks = []


        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

        """     
responsible for all the graphics within a game state
        """


def drawGameState(screen, gs):
    drawBoard(screen)   # function draws the squares on board
    # add in piece highlighting or suggested moves
    drawPieces(screen, gs.board)   # draw on top of squares

def drawBoard(screen):    # draws board using gamestate.board
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):  # draws pieces on the board
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not empty squares
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()