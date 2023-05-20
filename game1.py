import pygame
import os
from time import sleep

class Gra():

    def __init__(self, tablica, rozmiarEkran):
        self.tablica = tablica
        self.rozmiarEkran = rozmiarEkran
        self.pieceSize = self.rozmiarEkran[0] // self.tablica.getSize()[1], self.rozmiarEkran[1] // self.tablica.getSize()[0]
        self.obrazki()


    def run(self):
        pygame.init()
        self.ekran = pygame.display.set_mode(self.rozmiarEkran)
        petla = True
        while petla:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    petla = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if (self.tablica.getWon()):
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                sleep(3)
                petla =False

        pygame.quit()


    def draw(self):
        topLeft = (0, 0)
        for row in range(self.tablica.getSize()[0]):
            for col in range(self.tablica.getSize()[1]):
                piece = self.tablica.getPiece((row, col))
                image = self.getImage(piece)
                self.ekran.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]


    def obrazki(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image


    def getImage(self, piece):
        string = None
        if (piece.getClicked()):
            string = "iekliknienta-bomba" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "ekran"
        return self.images[string]

#mogę się dowiedzieć który przycisk jest naciskany
    def handleClick(self, position, rightClick):
        if (self.tablica.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.tablica.getPiece(index)
        self.tablica.handleClick(piece, rightClick)



