import sys, pygame
from pygame.locals import QUIT
import GameManager

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 640

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

DELTATIME = 0

GAME_MANAGER = GameManager.GameManager((WINDOW_WIDTH, WINDOW_HEIGHT))

DRAWABLES = []
MOVABLES = []
ATTACKS = []

SCREEN = pygame.display.set_mode((0, 0))

def run_game():
    #init game engine
    pygame.init()
    pygame.font.init()
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    SCREEN = pygame.display.set_mode(window_size)
    pygame.display.set_caption("A game")
    clock = pygame.time.Clock()
    fps = 60
    for cell in GAME_MANAGER.mimic_area.cells:
        DRAWABLES.append(cell)
    DRAWABLES.append(GAME_MANAGER.mimic)
    MOVABLES.append(GAME_MANAGER.mimic)

    # game loop
    while True:
        global DELTATIME
        DELTATIME = clock.tick(fps)
        SCREEN.fill((0,0,0))

        # terminate on quit-event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    on_arrow_key_pressed("left")
                elif event.key == pygame.K_RIGHT:
                    on_arrow_key_pressed("right")
                elif event.key == pygame.K_UP:
                    on_arrow_key_pressed("up")
                if event.key == pygame.K_DOWN:
                    on_arrow_key_pressed("down")
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # draw stuff
        move_movables()
        do_attack()
        draw()
        increase_attack_speed_loop()

        # update the screen
        pygame.display.update()

def draw():
    for drawable in DRAWABLES:
        pygame.draw.rect(
        SCREEN,
        drawable.color,
        drawable.get_rect(),
        drawable.border_width
    )

def move_movables():
    for m in MOVABLES:
        if m.is_moving:
            m.move()

def on_arrow_key_pressed(direction):
    # do mimic stuff
    if not GAME_MANAGER.mimic.is_moving:
        target_cell = GAME_MANAGER.get_neighbor_cell(direction)
        if target_cell is not None:
            GAME_MANAGER.mimic.start_moving(target_cell)

attack_interval = 2000
ms_since_last_attack = 0
active_attacks = []

def do_attack():
    global active_attacks
    global attack_interval
    global ms_since_last_attack
    active_attacks = list(filter(lambda x: getattr(x, "attack_complete") == False, active_attacks))
    ms_since_last_attack += DELTATIME
    if ms_since_last_attack >= attack_interval:
        ms_since_last_attack = 0
        random_cell = GAME_MANAGER.get_random_cell()
        active_attacks.append(GAME_MANAGER.get_attack_cell_for_cell(random_cell))
    
    for attack in active_attacks:
        pygame.draw.rect(
            SCREEN,
            attack.add_color(5),
            attack.get_rect(),
            0
        )

ms_since_attack_speed_increase = 0

def increase_attack_speed_loop():
    global ms_since_attack_speed_increase
    global attack_interval
    ms_since_attack_speed_increase += DELTATIME
    if ms_since_attack_speed_increase > 3000:
        ms_since_attack_speed_increase = 0
        attack_interval = max(250, attack_interval-250)

run_game()
