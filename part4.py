###Paste outside of gameplay loop (replace enemy object creation from part 3)

## PART 4A: Enemy types and spawn settings
# Each enemy object describes a size and color. There is one type for now.
enemy_objects = [
    {"width": 70, "height": 45, "color": (128, 0, 128)},
]
SPAWN_RATE = 1.0  # Fish per second. Higher numbers spawn more often.
FISH_SPEED = 5  # Pixels per frame moving left, at 60 FPS.
spawn_interval = 1000 / SPAWN_RATE  # Convert fish per second to milliseconds.
active_fish = []  # The fish currently moving across the scene.
start_time = pygame.time.get_ticks()
last_spawn_time = start_time
score = 0.0

## PART 4B: Spawn a fish just outside the right edge
def spawn_fish(enemy_objects):
    enemy_type = random.choice(enemy_objects)
    spawn_y = random.randint(0, ground.top - enemy_type["height"])
    fish_rect = pygame.Rect(
        screen.get_width(), spawn_y,
        enemy_type["width"], enemy_type["height"],
    )
    return {"rect": fish_rect, "color": enemy_type["color"]}



    
    
###Paste inside loop under if game is not over condition

## PART 4C: Spawn, move, and remove fish 
now = pygame.time.get_ticks()
if now - last_spawn_time >= spawn_interval:
    active_fish.append(spawn_fish(enemy_objects))
    last_spawn_time = now

for fish in active_fish:
    fish["rect"].x -= FISH_SPEED

# Keep only fish that have not completely left the screen.
active_fish = [fish for fish in active_fish if fish["rect"].right > 0]

## PART 4D: Track survival time and check collisions 
# This block stops updating when game_over is True, freezing the score.
score = (now - start_time) / 1000
for fish in active_fish:
    if player.colliderect(fish["rect"]):
        game_over = True
        break







###Paste at the bottom of loop (replace the previous enemy rendering):

## PART 4E: Draw all fish and the survival score
for fish in active_fish:
    pygame.draw.rect(screen, fish["color"], fish["rect"])
    score_text = font.render(f"Time: {score:.1f} seconds", True, "white")
    screen.blit(score_text, (20, 20))
