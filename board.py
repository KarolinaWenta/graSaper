from piece import Piece
from random import random
class Board():
    rozmiar = 0

#tutaj sobie przechowuje zmienne
    def __init__(self, rozmiar, prob):
        self.rozmiar = rozmiar
        self.prob = prob
        self.lost = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.ustawionaTablica()


    def ustawionaTablica(self):
        self.board = []
        for row in range(self.rozmiar[0]):
            row = []
            for col in range(self.rozmiar[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()


    def setNeighbors(self):
        for row in range(self.rozmiar[0]):
            for col in range(self.rozmiar[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)


    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0]+2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.rozmiar[0] or col < 0 or col >= self.rozmiar[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors


    def getSize(self):
        return self.rozmiar


    def getPiece(self, index):
        return self.board[index[0]][index[1]]


    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if (flag):
            piece.toggleFlag()
            return
        piece.click()
        if (piece.getHasBomb()):
            self.lost = True
            return
        self.numClicked += 1
        if (piece.getNumAround() != 0):
            return
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getClicked()):
                self.handleClick(neighbor, False)


    def getLost(self):
        return self.lost


    def getWon(self):
        return self.numNonBombs == self.numClicked



