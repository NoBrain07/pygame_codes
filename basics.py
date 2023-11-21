import pygame
from pygame.locals import *

pygame.init()

screen_size = (1080, 600)
color = "red"
color_shape_1 = "green"
color_shape_2 = "blue"
color_shape_3 = "purple"
color_shape_4 = "white"
screen = pygame.display.set_mode(screen_size)
og_image = pygame.image.load("interesting-pictures-blizka-monument-bulgaria.jpg")
image = pygame.transform.scale(og_image, (840, 360))
pygame.display.set_caption("Wow games")
clock = pygame.time.Clock()


def screen_set():
    screen.fill(color)

    pygame.draw.rect(screen, color_shape_1, pygame.Rect(20, 20, 1040, 560))
    pygame.draw.rect(screen, color_shape_2, pygame.Rect(40, 40, 1000, 520))
    pygame.draw.rect(screen, color_shape_3, pygame.Rect(60, 60, 960, 480))
    pygame.draw.rect(screen, color_shape_4, pygame.Rect(80, 80, 920, 440))


def run():
    game_status = True
    while game_status:
        screen.fill(color)
        screen_set()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    game_status = False
                elif event.key == K_LSHIFT or event.key == K_SPACE:
                    screen.blit(image, (120, 120))
        clock.tick(5)
        pygame.display.flip()
    pygame.quit()


run()
