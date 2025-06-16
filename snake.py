from random import randrange, choice
from turtle import *
from freegames import square, vector

# --- Collision constants ---
# --- Constantes de colisión ---
OBSTACLE_RADIUS = 20  # Radio to detect collision with obstacles / Radio para detectar colisión con obstáculos
FOOD_RADIUS = 6       # Radio to detect collision with food /  Radio para detectar colisión con comida

# --- Global game variables ---
# --- Variables globales del juego ---
food = vector(0, 0)              # Food position # Posición de la comida
snake = [vector(10, 0)]          # Snake segments list # Lista de segmentos de la serpiente
aim = vector(0, -10)             # direction of the snake # Dirección de la serpiente
obstacles = []                   # List of obstacles # Lista de obstáculos
speed = 100                      # Game speed in milliseconds # Velocidad del juego en milisegundos
score = 0                        # Game score # Puntaje del juego # Puntuación del juego
last_obstacle_addition = 0       # Last score at which an obstacle was added # Último puntaje en el que se agregó un obstáculo
game_over = False                # Game over flag # Bandera de fin de juego

def generate_obstacles(amount):
    """Generate a list of obstacles at random positions."""
    """Genera una lista de obstáculos en posiciones aleatorias."""
    obs = []
    for _ in range(amount):
        x = randrange(-15, 15) * 10
        y = randrange(-15, 15) * 10
        pos = vector(x, y)
        # Check that the position does not overlap with existing obstacles, snake segments, or food 
        # Verifica que la posición no se superponga con obstáculos existentes, segmentos de la serpiente o comida
        if (all(not is_collision(pos, o, OBSTACLE_RADIUS) for o in obs) and
            all(not is_collision(pos, s, OBSTACLE_RADIUS) for s in snake) and
            not is_collision(pos, food, OBSTACLE_RADIUS)):
            obs.append(pos)
    return obs

def change(x, y):
    """Snake direction change."""
    """Cambio de dirección de la serpiente."""
    aim.x = x
    aim.y = y

def draw_obstacles():
    """Draw obstacles on the screen."""
    """Dibuja los obstáculos en la pantalla."""
    for obstacle in obstacles:
        up()
        goto(obstacle.x, obstacle.y)
        down()
        color('green')
        begin_fill()
        circle(10)
        end_fill()

def add_obstacle():
    """Adds a new obstacle at a random position."""
    """Agrega un nuevo obstáculo en una posición aleatoria."""
    max_attempts = 100
    attempts = 0
    while attempts < max_attempts:
        x = randrange(-15, 15) * 10
        y = randrange(-15, 15) * 10
        pos = vector(x, y)
        # Check that the position does not overlap with existing obstacles, snake segments, or food
        # Verifica que la posición no se superponga con obstáculos existentes, segmentos de la serpiente o comida
        if (all(not is_collision(pos, obs, OBSTACLE_RADIUS) for obs in obstacles) and
            all(not is_collision(pos, s, OBSTACLE_RADIUS) for s in snake) and
            not is_collision(pos, food, OBSTACLE_RADIUS)):
            obstacles.append(pos)
            break
        attempts += 1

def move_obstacles():
    """Moves each obstacle in a random direction if possible."""
    """Mueve cada obstáculo en una dirección aleatoria si es posible."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    for i in range(len(obstacles)):
        move_dir = choice(directions)
        new_pos = obstacles[i] + move_dir
        # Check that the new position is within bounds and does not collide with other obstacles, snake, or food
        # Verifica que la nueva posición esté dentro de los límites y no colisione con otros obstáculos, la serpiente o la comida
        if (-200 < new_pos.x < 190 and -200 < new_pos.y < 190 and
            all(not is_collision(new_pos, obs, OBSTACLE_RADIUS) for j, obs in enumerate(obstacles) if j != i) and
            all(not is_collision(new_pos, s, OBSTACLE_RADIUS) for s in snake) and
            not is_collision(new_pos, food, OBSTACLE_RADIUS)):
            obstacles[i] = new_pos

def is_collision(a, b, radius):
    """Checks if two vectors collide within a given radius."""
    """Verifica si dos vectores colisionan dentro de un radio dado."""
    return abs(a.x - b.x) < radius and abs(a.y - b.y) < radius

def is_food_collision(head, food, radius=FOOD_RADIUS):
    """Checks if the snake's head collides with the food."""
    """Verifica si la cabeza de la serpiente colisiona con la comida."""
    return is_collision(head, food, radius)

def inside(head):
    """Checks if the snake's head is within the game boundaries."""
    """Verifica si la cabeza de la serpiente está dentro de los límites del juego."""
    return -200 < head.x < 190 and -200 < head.y < 190

def get_snake_color():
    """Determines the color of the snake based on its length."""
    """Determina el color de la serpiente según su longitud."""
    length = len(snake)
    if length < 10:
        return 'black'
    elif length < 20:
        return 'blue'
    elif length < 35:
        return 'green'
    else:
        return 'orange'

def move_food():
    """Moves the food to a new position if the score is 10 or more."""
    """Mueve la comida a una nueva posición si la puntuación es 10 o más."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_dir = choice(directions)
    new_pos = food + move_dir
    if -200 < new_pos.x < 190 and -200 < new_pos.y < 190:
        food.x = new_pos.x
        food.y = new_pos.y

def show_game_over():
    """Displays the game over message."""
    """Muestra el mensaje de fin de juego."""
    bgcolor('black')
    up()
    goto(0, 0)
    color('red')
    write(f'Game Over!\nScore: {score}\nPress R to restart', align='center', font=('Arial', 18, 'bold'))

def restart_game():
    """Restarts the game by resetting all variables and clearing the screen."""
    """Reinicia el juego reiniciando todas las variables y limpiando la pantalla."""
    global food, snake, aim, obstacles, speed, score, last_obstacle_addition, game_over
    bgcolor('white')
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    num_obstacles = randrange(1, 11)
    obstacles.clear()
    obstacles.extend(generate_obstacles(num_obstacles))
    speed = 100
    score = 0
    last_obstacle_addition = 0
    game_over = False
    clear()
    move()

def flash_red_then_game_over():
    """Flashes red before showing Game Over."""
    """Hace un flash rojo antes de mostrar Game Over."""
    bgcolor('red')
    update()
    ontimer(show_game_over, 300)

def food_flash_effect(times=3, delay=80):
    """Flashes the food before it disappears."""
    """Hace parpadear la comida antes de desaparecer."""
    for i in range(times): 
        ontimer(lambda: square(food.x, food.y, 9, 'yellow'), delay * (2 * i))
        ontimer(lambda: square(food.x, food.y, 9, 'purple'), delay * (2 * i + 1))

def update_food_position():
    """Updates the food position and continues the game."""
    """Actualiza la posición de la comida y continúa el juego."""
    while True:
        new_x = randrange(-15, 15) * 10
        new_y = randrange(-15, 15) * 10
        new_pos = vector(new_x, new_y)
        # Verifica que la nueva posición no esté ocupada 
        # Check that the new position is not occupied by obstacles, snake segments, or food
        if (not any(is_collision(new_pos, obs, OBSTACLE_RADIUS) for obs in obstacles) and
            not any(is_collision(new_pos, s, FOOD_RADIUS) for s in snake)):
            food.x = new_x
            food.y = new_y
            break
    ontimer(move, speed)

def move():
    """Mueve la serpiente un segmento hacia adelante."""
    """Moves the snake one segment forward."""
    global speed, score, last_obstacle_addition, game_over
    if game_over:
        return
    head = snake[-1].copy()
    head.move(aim)

    # Check for collisions with boundaries, body, or obstacles
    # Verifica colisiones con límites, cuerpo u obstáculos
    if not inside(head) or head in snake or any(is_collision(head, obs, OBSTACLE_RADIUS) for obs in obstacles):
        square(head.x, head.y, 9, 'red')
        update()
        flash_red_then_game_over()
        game_over = True
        return

    snake.append(head)

    # Add obstacles every 7 points
    # Agrega obstáculos cada 7 puntos
    if score % 7 == 0 and score != 0 and score != last_obstacle_addition:
        add_obstacle()
        last_obstacle_addition = score

    # Move food if score is 10 or more
    # Mueve la comida si el score es 10 o más
    if score >= 10:
        move_food()

    # Effect when eating food
    # Efecto al comer comida
    if is_food_collision(head, food):
        score += 1
        print('Snake:', len(snake), 'Score:', score)
        food_flash_effect()
        ontimer(update_food_position, 3 * 80 * 2)
        return
    else:
        snake.pop(0)

    clear()
    move_obstacles()
    draw_obstacles()
    
    for body in snake:
        square(body.x, body.y, 9, get_snake_color())

    square(food.x, food.y, 9, 'purple')
    update()
    ontimer(move, speed)

# --- Configuración de la ventana y controles ---
# --- Window setup and controls ---
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(restart_game, 'r')
restart_game()
done()
