from game1 import Gra
from board import Board
rozmiar = (9, 9)
prob = 0.1
tablica = Board(rozmiar, prob)
rozmiarEkran = (800, 800)
game1 = Gra(tablica, rozmiarEkran)
game1.run()