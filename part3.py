###Paste outside of loop:

## PART 3A: 
## Create the enemy and reset positions
player_start = player.topleft
game_over = False
font = pygame.font.Font(None, 48)
enemy = pygame.Rect(900, 0, 70, 45)
enemy.centery = screen.get_rect().centery
enemy_start = enemy.topleft
enemy_color = (128, 0, 128)





###paste within gameplay loop

## PART 3B: Press Space to reset after a collision
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                player.topleft = player_start
                game_over = False
                
                
                



###Add condition to existing code

if not game_over:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= player_speed  # Up
    if keys[pygame.K_d]:
        player.x += player_speed  # Right
    if keys[pygame.K_s]:
        player.y += player_speed  # Down
    if keys[pygame.K_a]:
        player.x -= player_speed  # Left
            
	# Keep the player inside the water, above the sand.
    water_area = pygame.Rect(0, 0, screen.get_width(), ground.top)
    player.clamp_ip(water_area)
    
    ## PART 3C: Stop the game when the rectangles overlap
    if player.colliderect(enemy):
        game_over = True
        






###paste at bottom:

# Part 3D: Show the restart message after a collision.
    pygame.draw.rect(screen, enemy_color, enemy)

    if game_over:
        message = font.render("Game over! Press Space to restart", True, "white")
        message_rect = message.get_rect(center=(screen.get_width() // 2, 100))
        screen.blit(message, message_rect)

