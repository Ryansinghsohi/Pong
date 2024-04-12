import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    K_w,
    K_s,
    KEYDOWN,
    QUIT,
)

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Pong")

player_x_1 = SCREEN_WIDTH - 30
player_y_1 = SCREEN_HEIGHT // 2

player_x_2 = 30
player_y_2 = SCREEN_HEIGHT // 2

ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_radius = 10
global ball_bounce_speed
ball_bounce_speed = 1

ball_y_speed = 0.2 * ball_bounce_speed
ball_x_speed = 0.2 * ball_bounce_speed


def updateSpeed():
    global ball_bounce_speed, ball_x_speed, ball_y_speed  # Declare as global to modify the variables
    ball_bounce_speed += 0.1  # Increment the bounce speed
    ball_x_speed = 0.2 * ball_bounce_speed
    ball_y_speed = 0.2 * ball_bounce_speed


# Display the score
player_1_score = 0
player_2_score = 0
font = pg.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Event handling
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            # Player movement controls
            if event.key == K_DOWN:
                player_y_1 += 30
            if event.key == K_UP:
                player_y_1 -= 30
            if event.key == K_w:
                player_y_2 -= 30
            if event.key == K_s:
                player_y_2 += 30
            if event.key == K_ESCAPE:
                running = False

    # Ball movement and collision detection
    ball_y += ball_y_speed
    ball_x += ball_x_speed
    # Bounce off top and bottom
    if ball_y < 0 + ball_radius or ball_y > SCREEN_HEIGHT - ball_radius:
        ball_y_speed *= -1
    # Scoring
    if ball_x > SCREEN_WIDTH + ball_radius:
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        player_2_score += 1
        ball_bounce_speed = 1
    if ball_x < 0 - ball_radius:
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        player_1_score += 1
        ball_bounce_speed = 1
    # Ball hitting paddles
    if (player_x_1 - 30 <= ball_x <= player_x_1) and (player_y_1 - 75 <= ball_y <= player_y_1):
        ball_x_speed *= -1
        updateSpeed()  # Update the speed after a hit
    if (player_x_2 <= ball_x <= player_x_2 + 10) and (player_y_2 - 75 < ball_y < player_y_2):
        ball_x_speed *= -1
        updateSpeed()  # Update the speed after a hit

    # Update the display
    screen.fill((255, 255, 255))
    text_score_1 = font.render(f"{player_1_score}", True, (0, 0, 0), (255, 255, 255))
    text_score_2 = font.render(f"{player_2_score}", True, (0, 0, 0), (255, 255, 255))
    textRect_1 = text_score_1.get_rect(center=(SCREEN_WIDTH // 2 + 30, 50))
    textRect_2 = text_score_2.get_rect(center=(SCREEN_WIDTH // 2 - 30, 50))
    screen.blit(text_score_1, textRect_1)
    screen.blit(text_score_2, textRect_2)
    pg.draw.circle(screen, (0, 0, 0), (ball_x, ball_y), ball_radius)
    pg.draw.line(screen, (0, 0, 0), (player_x_2, player_y_2), (player_x_2, player_y_2 - 75), 10)
    pg.draw.line(screen, (0, 0, 0), (player_x_1, player_y_1), (player_x_1, player_y_1 - 75), 10)
    pg.display.flip()
