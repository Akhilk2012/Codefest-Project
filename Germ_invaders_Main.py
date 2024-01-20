import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

icon = pygame.image.load("icon.png")

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Germ Invaders")
pygame.display.set_icon(icon)