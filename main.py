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
    GAME_MANAGER.start()
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
                if event.key == pygame.K_ESCAPE:
                    GAME_MANAGER.toggle_pause()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # draw stuff
        if not GAME_MANAGER.is_game_over and not GAME_MANAGER.is_paused:
            do_attack()
            move_movables()
            draw()
            GAME_MANAGER.check_mimic_collisions()
        elif GAME_MANAGER.is_paused:
            pass
        else:
            pass

        if not GAME_MANAGER.is_paused and not GAME_MANAGER.is_game_over:
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

def do_attack():
    attack_controller = GAME_MANAGER.attack_controller
    attack_controller.update(DELTATIME)
    if attack_controller.ms_since_last_attack >= attack_controller.attack_interval:
        attack_controller.attack_cell(GAME_MANAGER.get_random_cell())
    
    for attack in attack_controller.active_attacks:
        pygame.draw.rect(
            SCREEN,
            attack.add_color(5),
            attack.get_rect(),
            0
        )

run_game()
