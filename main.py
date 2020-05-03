import sys, pygame
from pygame.locals import QUIT
import GameManager

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 640

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

GAME_MANAGER = GameManager.GameManager((WINDOW_WIDTH, WINDOW_HEIGHT))

DRAWABLES = []

def run_game():
    #init game engine
    pygame.init()
    pygame.font.init()
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("A game")
    clock = pygame.time.Clock()
    frame = 0
    fps = 60
    for cell in GAME_MANAGER.mimic_area.cells:
        DRAWABLES.append(cell)
    DRAWABLES.append(GAME_MANAGER.mimic)

    # game loop
    while True:
        frame += 1
        screen.fill((0,0,0))

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
        #draw_mimic_area(screen)
        #draw_mimic(screen, GAME_MANAGER.mimic)
        mimic = GAME_MANAGER.mimic
        if (mimic.is_moving):
            mimic.move()
        draw(screen)
        if frame / fps == 5:
            do_attack()

        # update the screen
        pygame.display.update()
        clock.tick(fps)

def draw(screen):
    for drawable in DRAWABLES:
        pygame.draw.rect(
        screen,
        drawable.color,
        drawable.get_rect(),
        drawable.border_width
    )

def on_arrow_key_pressed(direction):
    # do mimic stuff
    if not GAME_MANAGER.mimic.is_moving:
        target_cell = GAME_MANAGER.get_neighbor_cell(direction)
        if target_cell is not None:
            GAME_MANAGER.mimic.start_moving(target_cell)

def do_attack():
    attack_beam = GAME_MANAGER.generate_attack_beam()

run_game()
