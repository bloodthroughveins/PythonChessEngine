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
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"], ]
        self.whiteToMove = True
        self.moveLog = []

