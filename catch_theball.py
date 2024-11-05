import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catch the Ball')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up clock
clock = pygame.time.Clock()

# Paddle settings
paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 30
paddle_speed = 10

# Ball settings
ball_size = 20
ball_x = random.randint(0, screen_width - ball_size)
ball_y = 0
ball_speed = 3

# Score and game over flag
score = 0
game_over = False

# Font for text
font = pygame.font.SysFont(None, 35)

# Function to display text
def display_message(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

# Main game loop
def game_loop():
    global paddle_x, ball_x, ball_y, ball_speed, score, game_over

    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # Ball movement
        ball_y += ball_speed

        # Check if ball hits the paddle
        if paddle_y < ball_y + ball_size < paddle_y + paddle_height and paddle_x < ball_x + ball_size < paddle_x + paddle_width:
            score += 1
            ball_speed += 1
            ball_x = random.randint(0, screen_width - ball_size)
            ball_y = 0

        # Reset ball if it hits the ground
        if ball_y > screen_height:
            game_over = True

        # Fill the screen with white
        screen.fill(white)

        # Draw the paddle
        pygame.draw.rect(screen, black, [paddle_x, paddle_y, paddle_width, paddle_height])

        # Draw the ball
        pygame.draw.ellipse(screen, red, [ball_x, ball_y, ball_size, ball_size])

        # Display score
        display_message(f'Score: {score}', black, 10, 10)

        # Update the display
        pygame.display.update()

        # Limit frames per second
        clock.tick(60)

    # Game over message
    screen.fill(white)
    display_message(f'Game Over! Final Score: {score}', red, screen_width // 4, screen_height // 2)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

# Start the game
game_loop()