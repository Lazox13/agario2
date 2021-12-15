import random
import pygame
from pygame import Vector2

from joueur import Joueur


class Ennemi():

    def __init__(self):
        self.position = Vector2(random.randint(0, 800), random.randint(0, 800))
        self.couleur = (255,0,0)
        self.rayon = 10
        self.rayon_max = 150

        self.raideur = 0.035
        self.vitesse = 1
        self.vitessemax = 5
        self.direction = Vector2(0,0)
        self.Ux = Vector2(0,0)
        self.l = 0
        self.l0 = 10
        self.L = 0
        self.Fx = 0



    def grossir(self):
        if self.rayon < 150 :
            self.rayon = self.rayon + 1

            self.vitessemax = self.vitessemax * 0.988
            self.Fx = self.vitesse * self.Fx

    def dead(self):
        self.position = Vector2(random.randint(0, 800), random.randint(0, 800))

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

    def deplacer(self,joueur):
        if self.position.y < 0 or self.position.y > 800:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)
            self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.position.x < 0 or self.position.x > 800:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)
            self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.direction = joueur.position - self.position