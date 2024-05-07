import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    K_w,
    K_s,
    KEYDOWN,
    KEYUP,
    QUIT,
)

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Pong")

# player 1 variables
player_x_1 = SCREEN_WIDTH - 30
player_y_1 = SCREEN_HEIGHT // 2
player_1_score = 0

# player 2 variables
player_x_2 = 30
player_y_2 = SCREEN_HEIGHT // 2
player_2_score = 0

# player variebel
player_height = 75

# ball variables
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_radius = 10
ball_speed = 0.5

ball_y_speed = 0.2 * ball_speed
ball_x_speed = 0.2 * ball_speed


# function to have the ball's speed flipped if it hits the player
def update_speed():
    global ball_x_speed, ball_y_speed, ball_speed
    ball_speed += 1
    ball_x_speed = 0.1 * ball_speed * (-1 if ball_x_speed < 0 else 1)  # maintain direction when speeding up
    ball_y_speed = 0.1 * ball_speed * (-1 if ball_y_speed < 0 else 1)


# Flags to track continuous movement
move_up_1 = False
move_down_1 = False
move_up_2 = False
move_down_2 = False

# Movement speeds
player_speed = 0.5  # Adjust speed as needed

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
                move_down_1 = True
            elif event.key == K_UP:
                move_up_1 = True
            elif event.key == K_w:
                move_up_2 = True
            elif event.key == K_s:
                move_down_2 = True
            elif event.key == K_ESCAPE:
                running = False
        if event.type == KEYUP:
            if event.key == K_DOWN:
                move_down_1 = False
            elif event.key == K_UP:
                move_up_1 = False
            elif event.key == K_w:
                move_up_2 = False
            elif event.key == K_s:
                move_down_2 = False

    # Continuous movement for player 1
    if move_down_1:
        player_y_1 += player_speed
    if move_up_1:
        player_y_1 -= player_speed

    # Continuous movement for player 2
    if move_down_2:
        player_y_2 += player_speed
    if move_up_2:
        player_y_2 -= player_speed

    # the ball's movement
    ball_y += ball_y_speed
    ball_x += ball_x_speed

    # ball hits the floor or roof
    if ball_y <= 0 + ball_radius or ball_y >= SCREEN_HEIGHT - ball_radius:
        ball_y_speed *= -1

    # player 2 scores
    if ball_x >= SCREEN_WIDTH - ball_radius:
        player_2_score += 1
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_speed = 0.75
        ball_x_speed = 0.2 * ball_speed  # reset speed to the right
        ball_y_speed = 0.2 * ball_speed
        player_y_1, player_y_2 = SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2

    # player 1 scores
    if ball_x <= 0 + ball_radius:
        player_1_score += 1
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_speed = 0.75
        ball_x_speed = -0.2 * ball_speed  # reset speed to the left
        ball_y_speed = 0.2 * ball_speed
        player_y_1, player_y_2 = SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2

    # Collision with Player 1
    if (
        (player_x_1 - 1 <= ball_x + ball_radius <= player_x_1)
        and (player_y_1 - 75 - ball_radius <= ball_y <= player_y_1 + ball_radius)
    ):
        ball_x_speed *= -1
        update_speed()

    # Collision with Player 2
    if (
        (player_x_2 <= ball_x - ball_radius <= player_x_2 + 1)
        and (player_y_2 - 75 - ball_radius <= ball_y <= player_y_2 + ball_radius)
    ):
        ball_x_speed *= -1
        update_speed()

    # player borders
    # player 1 top border
    if player_y_1 < 0 + player_height:
        player_y_1 = 0 + player_height

    # player 1 bottom border
    if player_y_1 > SCREEN_HEIGHT:
        player_y_1 = SCREEN_HEIGHT

    # player 2 top border
    if player_y_2 < 0 + player_height:
        player_y_2 = 0 + player_height

    # player 2 bottom border
    if player_y_2 > SCREEN_HEIGHT:
        player_y_2 = SCREEN_HEIGHT

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
    pg.draw.line(screen, (0, 0, 0), (player_x_2, player_y_2), (player_x_2, player_y_2 - player_height), 10)
    pg.draw.line(screen, (0, 0, 0), (player_x_1, player_y_1), (player_x_1, player_y_1 - player_height), 10)
    pg.display.flip()

pg.quit()
