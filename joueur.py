import random
import pygame
from pygame import Vector2

class Joueur():

    def __init__(self):
        self.position = Vector2(random.randint(0, 800), random.randint(0, 800))
        self.couleur = self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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

    def mourir(self):
        #self.rayon = 2
        exit("GAMEOVER: Vous avez perdu!")


    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

    def deplacer(self,clic, h = 800, l = 800):

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)
            self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)
            self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


        if clic is not None:

            self.Ux = clic - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)


        if self.direction.length() > self.vitessemax and self.direction.length() !=0 :
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position