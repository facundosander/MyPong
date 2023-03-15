import pygame
import random

# Inicializar Pygame
pygame.init()

#Definir clock
clock = pygame.time.Clock()

# Definir las dimensiones de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Definir los colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir las constantes del juego
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 100
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
LEFT = False
RIGHT = True
BALL_SPEED = 5
PADDLE_SPEED = 50

# Definir las variables del juego
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([BALL_SPEED, -BALL_SPEED]), random.choice([BALL_SPEED, -BALL_SPEED])]
paddle1_pos = HEIGHT // 2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT // 2 - HALF_PAD_HEIGHT
score1 = 0
score2 = 0
game_over = False

# Dibujar la pelota
def draw_ball(ball_pos):
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)

# Dibujar las paletas
def draw_paddles(paddle1_pos, paddle2_pos):
    pygame.draw.rect(screen, WHITE, (0, paddle1_pos, PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PAD_WIDTH, paddle2_pos, PAD_WIDTH, PAD_HEIGHT))

# Actualizar la posición de la pelota
def update_ball(ball_pos, ball_vel):
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += 0.1 * ball_vel[0]
            ball_vel[1] += 0.1 * ball_vel[1]
        else:
            restart_ball(RIGHT)
            global score2
            score2 += 1
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += 0.1 * ball_vel[0]
            ball_vel[1] += 0.1 * ball_vel[1]
        else:
            restart_ball(LEFT)
            global score1
            score1 += 1
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

# Reiniciar la pelota
def restart_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    if direction == LEFT:
        ball_vel = [-BALL_SPEED, random.choice([BALL_SPEED, -BALL_SPEED])]
    elif direction == RIGHT:
        ball_vel = [BALL_SPEED, random.choice([BALL_SPEED, -BALL_SPEED])]
 #Actualizar la posición de la paleta
def update_paddle(paddle_pos, direction):
    if direction == "up":
      paddle_pos -= PADDLE_SPEED
    elif direction == "down":
      paddle_pos += PADDLE_SPEED
# Limitar la paleta dentro de los límites de la pantalla
    if paddle_pos < 0:
      paddle_pos = 0
    if paddle_pos > HEIGHT - PAD_HEIGHT:
      paddle_pos = HEIGHT - PAD_HEIGHT
    return paddle_pos

#Dibujar el marcador
def draw_score(score1, score2):
  font = pygame.font.Font(None, 36)
  text1 = font.render(str(score1), True, WHITE)
  text2 = font.render(str(score2), True, WHITE)
  screen.blit(text1, (WIDTH // 4, 50))
  screen.blit(text2, (WIDTH * 3 // 4, 50))

# Loop principal del juego
while not game_over:
    # Manejar eventos de entrada del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_pos = update_paddle(paddle1_pos, "up")
            if event.key == pygame.K_s:
                paddle1_pos = update_paddle(paddle1_pos, "down")
            if event.key == pygame.K_UP:
                paddle2_pos = update_paddle(paddle2_pos, "up")
            if event.key == pygame.K_DOWN:
                paddle2_pos = update_paddle(paddle2_pos, "down")

    # Actualizar la posición de la pelota y las paletas
    update_ball(ball_pos, ball_vel)
    paddle1_pos = update_paddle(paddle1_pos, "")
    paddle2_pos = update_paddle(paddle2_pos, "")

    # Dibujar el fondo, la pelota, las paletas y el marcador
    screen.fill(BLACK)
    draw_ball(ball_pos)
    draw_paddles(paddle1_pos, paddle2_pos)
    draw_score(score1, score2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    clock.tick(60)
#Finalizar Pygame
pygame.quit()