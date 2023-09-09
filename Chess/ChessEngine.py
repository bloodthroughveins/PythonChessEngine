"""
This class is gonna be whats responsible for storing all the information about the current state of the chess game
It will also be responsible for determining the valid moves at the current state
It will also be able to keep a move log too
"""


class GameState():  # their is most likely a way more efficient way to do this but this is simple lol
    # board is 8x8 2d list and each element of the list has 2 characters to represent it
    # 1st character represents the the color of the piece black or white
    # 2nd character represents the type of piece ex: king (K) or queen (Q)
    # 3rd "--" represents an empty space with no piece
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            # I believe a dash is a simple efficient way to represent a blank space
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            # May not be the best option but in a simple OOP program I believe it will do
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)   # log the move for later / option to swap for undo later
        self.whiteToMove = not self.whiteToMove # swap the players

class Move():
    # able to allow chess notation to python array location
    # shoutout some asian kid that i copied this dictionary from
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                   "5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0,"b":1,"c":2,"d":3,
                   "e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        #start location/square
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        # end location
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        #piece moved and or captured
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    def getChessNotation(self):
        #   add to make chess notation in future
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)


    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r] #  file than rank in row colum notation