import pygame

pygame.init()

## Create window to display game
screen = pygame.display.set_mode((1280,720))

## Create clock to keep track of timing
clock = pygame.time.Clock()

## Gameplay loop - updates every tick
running = True
while running:
    ## Game logic here
    ## Everything in this loop updates every frame
    ## Framerate can be customized with clock.tick(FPS)
    



    ## MUST STAY AT THE END
    pygame.display.flip()  ## Refresh on-screen display
    clock.tick(60)         ## wait until next frame (at 60 FPS)  


pygame.quit()
