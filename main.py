import sys, pygame
from pygame.locals import QUIT
import GameManager

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 640

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

GAME_MANAGER = GameManager.GameManager((WINDOW_WIDTH, WINDOW_HEIGHT))

def run_game():
    #init game engine
    pygame.init()
    pygame.font.init()
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("A game")
    clock = pygame.time.Clock()

    # game loop
    while True:
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
        draw_mimic_area(screen)
        draw_mimic(screen, GAME_MANAGER.mimic)

        # update the screen
        pygame.display.update()
        clock.tick(60)

def draw_mimic_area(screen):
    mimic_area = GAME_MANAGER.mimic_area

    for cell in mimic_area.cells:
        draw_cell_rect(screen, cell, 1)

def draw_mimic(screen, mimic):
    if (mimic.is_moving):
        mimic.move()
        
    pygame.draw.rect(
        screen,
        WHITE,
        mimic.get_rect(),
        0
    )

def on_arrow_key_pressed(direction):
    # do mimic stuff
    if not GAME_MANAGER.mimic.is_moving:
        target_cell = GAME_MANAGER.get_neighbor_cell(direction)
        if target_cell is not None:
            GAME_MANAGER.mimic.start_moving(target_cell)

def draw_cell_rect(screen, cell, border):
    pygame.draw.rect(
                screen,
                GRAY,
                cell.get_rect(),
                border
            )



run_game()
