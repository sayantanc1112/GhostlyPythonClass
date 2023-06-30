import pygame
import random

# Initialize the game
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up the game variables
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_size = 10
food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawned = True
direction = 'RIGHT'
change_to = direction
score = 0

# Set up the game clock
clock = pygame.time.Clock()
fps = 20

# Function to display the score
def show_score(color, font, size, score_value, x, y):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score_value), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (x, y)
    screen.blit(score_surface, score_rect)

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # Validate the direction input
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Move the snake
    if direction == 'RIGHT':
        snake_pos[0][0] += snake_size
    if direction == 'LEFT':
        snake_pos[0][0] -= snake_size
    if direction == 'UP':
        snake_pos[0][1] -= snake_size
    if direction == 'DOWN':
        snake_pos[0][1] += snake_size

    # Check if the snake hits the boundary
    if (
        snake_pos[0][0] >= width
        or snake_pos[0][0] < 0
        or snake_pos[0][1] >= height
        or snake_pos[0][1] < 0
    ):
        game_over = True

    # Check if the snake hits itself
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over = True

    # Check if the snake eats the food
    if snake_pos[0] == food_pos:
        score += 1
        food_spawned = False
    else:
        snake_pos.pop()

    # Spawn new food if needed
    if not food_spawned:
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        food_spawned = True

    # Clear the screen
    screen.fill(black)

    # Draw the snake
    for pos in snake_pos:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # Display the score
    show_score(white, "arial", 20, score, width // 2, 10)

    # Update the game display
    pygame.display.flip()

    # Control the game speed
    clock.tick(fps)

# Quit the game
pygame.quit()
