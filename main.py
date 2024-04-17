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

# player 1 variebls
player_x_1 = SCREEN_WIDTH - 30
player_y_1 = SCREEN_HEIGHT // 2
player_1_score = 0

# player 2 varibles
player_x_2 = 30
player_y_2 = SCREEN_HEIGHT // 2
player_2_score = 0

# ball variebels
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_radius = 10
ball_speed = 1

ball_y_speed = 0.2 * ball_speed
ball_x_speed = 0.2 * ball_speed

# function to have the balls speed fliped if it hits the player
def update_speed():
    global ball_x_speed, ball_y_speed, ball_speed
    ball_speed += 1
    ball_x_speed = 0.1 * ball_speed * (-1 if ball_x_speed < 0 else 1)  # maintain direction when speeding up
    ball_y_speed = 0.1 * ball_speed * (-1 if ball_y_speed < 0 else 1)

# score
font = pg.font.Font(None, 36)
textRect_1 = None
textRect_2 = None

running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                player_y_1 += 30
            elif event.key == K_UP:
                player_y_1 -= 30
            elif event.key == K_w:
                player_y_2 -= 30
            elif event.key == K_s:
                player_y_2 += 30
            elif event.key == K_ESCAPE:
                running = False

    # the balls force
    ball_y += ball_y_speed
    ball_x += ball_x_speed

    # ball hits the flore or roof
    if ball_y <= 0 + ball_radius or ball_y >= SCREEN_HEIGHT - ball_radius:
        ball_y_speed *= -1

    # player 2 scores
    if ball_x >= SCREEN_WIDTH - ball_radius:
        player_2_score += 1
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_speed = 1
        ball_x_speed = 0.2 * ball_speed  # reset speed to right
        ball_y_speed = 0.2 * ball_speed

    # player 1 scores
    if ball_x <= 0 + ball_radius:
        player_1_score += 1
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_speed = 1
        ball_x_speed = -0.2 * ball_speed  # reset speed to left
        ball_y_speed = 0.2 * ball_speed

    # Collision with Player 1
    if (player_x_1 - 10 <= ball_x + ball_radius <= player_x_1) and (player_y_1 - 75 <= ball_y <= player_y_1):
        ball_x_speed *= -1
        update_speed()

    # Collision with Player 2
    if (player_x_2 <= ball_x - ball_radius <= player_x_2 + 10) and (player_y_2 - 75 <= ball_y <= player_y_2):
        ball_x_speed *= -1
        update_speed()

    # fill the screen white
    screen.fill((255, 255, 255))
    # display score
    text_score_1 = font.render(f"{player_1_score}", True, (0, 0, 0), (255, 255, 255))
    text_score_2 = font.render(f"{player_2_score}", True, (0, 0, 0), (255, 255, 255))
    textRect_1 = text_score_1.get_rect(center=(SCREEN_WIDTH // 2 + 30, 50))
    textRect_2 = text_score_2.get_rect(center=(SCREEN_WIDTH // 2 - 30, 50))
    screen.blit(text_score_1, textRect_1)
    screen.blit(text_score_2, textRect_2)
    # display the ball
    pg.draw.circle(screen, (0, 0, 0), (ball_x, ball_y), ball_radius)
    # display the players
    pg.draw.line(screen, (0, 0, 0), (player_x_2, player_y_2), (player_x_2, player_y_2 - 75), 10)
    pg.draw.line(screen, (0, 0, 0), (player_x_1, player_y_1), (player_x_1, player_y_1 - 75), 10)
    pg.display.flip()

pg.quit()
