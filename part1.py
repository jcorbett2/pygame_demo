


###Paste above gameplay loop:

# Part 1A:
# Scene colors and sandy ground along the bottom.
water_color = (30, 144, 255)
sand_color = (194, 178, 128)
ground = pygame.Rect(0, 620, 1280, 100)





###Paste inside gameplay loop:

# Part 1B:
    ## Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ## If user presses escape then exit window
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False




            
###paste at the bottom of the gameplay loop:

screen.fill(water_color)
pygame.draw.rect(screen, sand_color, ground)
