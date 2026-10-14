###Paste above gameplay loop

## PART 2A: Create the player
## Use an red rectangle as our placeholder character.
player = pygame.Rect(20, 0, 60, 35)
player.centery = screen.get_rect().centery
player_color = (255, 0, 0)
player_speed = 5  ## Pixels per frame at 60 FPS.






###Paste inside gameplay loop

keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
    player.y -= player_speed  # Up
if keys[pygame.K_d]:
    player.x += player_speed  # Right
if keys[pygame.K_s]:
    player.y += player_speed  # Down
if keys[pygame.K_a]:
    player.x -= player_speed  # Left

## Keep the player inside the water, above the sand.
water_area = pygame.Rect(0, 0, screen.get_width(), ground.top)
player.clamp_ip(water_area)





###Paste at the bottom of gameplay loop BELOW THE SCREEN RENDERING:

## PART 2C: Draw the player 
pygame.draw.rect(screen, player_color, player)
