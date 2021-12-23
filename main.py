import pygame
from model.const import WITDH

WIN = pygame.display.set_mode((WITDH, WITDH))
pygame.display.set_caption("A* PATHFINDER")

def main():
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

main()