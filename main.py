#"They are totally given the right to quit" - LaRose
#"It still doesn't believe in pygame" - LaRose
#"Don't cause problems" - LaRose
#"Oh well, that's awkward" - LaRose
#"They're quite literally different" - LaRose
import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
game = Game("img/bird.png", "img/pipe.png", "img/background.png", "img/ground.png")
game.resize_img()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.show_background(screen)


    pygame.display.update()
    clock.tick(120)