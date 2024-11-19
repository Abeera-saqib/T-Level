import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Objects Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Gun parameters
gun_pos = (WIDTH // 2, HEIGHT - 50)
gun_color = GREEN
gun_length = 50
gun_angle = 0

# Bullet parameters
bullet_speed = 10
bullets = []

# Flying objects parameters
fly_objects = []
fly_object_radius = 20
fly_object_speed = 3
spawn_timer = 0
spawn_interval = 60

# Score counter
score = 0
font = pygame.font.Font(None, 36)

# Function to rotate the gun based on the mouse position
def rotate_gun(gun_pos, mouse_pos):
    dx = mouse_pos[0] - gun_pos[0]
    dy = mouse_pos[1] - gun_pos[1]
    angle = math.atan2(dy, dx)
    return angle

# Function to shoot bullets
def shoot_bullet(gun_pos, angle):
    bullet_dx = bullet_speed * math.cos(angle)
    bullet_dy = bullet_speed * math.sin(angle)
    bullet = {'pos': list(gun_pos), 'dx': bullet_dx, 'dy': bullet_dy}
    bullets.append(bullet)

# Function to spawn flying objects
def spawn_fly_object():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT // 2)
    fly_objects.append({'pos': [x, y], 'dx': random.choice([-1, 1]) * fly_object_speed,
                        'dy': random.choice([-1, 1]) * fly_object_speed})

# Function to display score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Get the mouse position and calculate the gun angle
    mouse_pos = pygame.mouse.get_pos()
    gun_angle = rotate_gun(gun_pos, mouse_pos)

    # Draw the rotating gun
    gun_end = (gun_pos[0] + gun_length * math.cos(gun_angle),
               gun_pos[1] + gun_length * math.sin(gun_angle))
    pygame.draw.line(screen, gun_color, gun_pos, gun_end, 5)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot bullet on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot_bullet(gun_pos, gun_angle)

    # Update bullet positions
    for bullet in bullets[:]:
        bullet['pos'][0] += bullet['dx']
        bullet['pos'][1] += bullet['dy']
        pygame.draw.circle(screen, RED, (int(bullet['pos'][0]), int(bullet['pos'][1])), 5)

        # Remove bullets that leave the screen
        if (bullet['pos'][0] < 0 or bullet['pos'][0] > WIDTH or
                bullet['pos'][1] < 0 or bullet['pos'][1] > HEIGHT):
            bullets.remove(bullet)

    # Spawn flying objects at intervals
    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        spawn_fly_object()
        spawn_timer = 0

    # Update flying objects positions
    for obj in fly_objects[:]:
        obj['pos'][0] += obj['dx']
        obj['pos'][1] += obj['dy']

        # Keep flying objects within bounds
        if obj['pos'][0] - fly_object_radius < 0 or obj['pos'][0] + fly_object_radius > WIDTH:
            obj['dx'] = -obj['dx']
        if obj['pos'][1] - fly_object_radius < 0 or obj['pos'][1] + fly_object_radius > HEIGHT:
            obj['dy'] = -obj['dy']

        pygame.draw.circle(screen, BLUE, (int(obj['pos'][0]), int(obj['pos'][1])), fly_object_radius)

    # Check for bullet collisions with flying objects
    for obj in fly_objects[:]:
        for bullet in bullets[:]:
            distance = math.hypot(obj['pos'][0] - bullet['pos'][0], obj['pos'][1] - bullet['pos'][1])
            if distance < fly_object_radius:
                fly_objects.remove(obj)
                bullets.remove(bullet)
                score += 1

    # Display the score
    display_score(score)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    
# Quit pygame
pygame.quit()
