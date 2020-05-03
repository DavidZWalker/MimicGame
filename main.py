import sys, pygame
from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEBUTTONDOWN
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
            if event.type == MOUSEBUTTONUP:
                on_mouse_up()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # draw stuff
        draw_interaction_area(screen)
        draw_mimic_area(screen)
        draw_mimic(screen, GAME_MANAGER.mimic)
        handle_mouse(screen)

        # update the screen
        pygame.display.update()
        clock.tick(60)

def draw_mimic_area(screen):
    mimic_area = GAME_MANAGER.get_mimic_area()

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

def draw_interaction_area(screen):
    i_border = GAME_MANAGER.get_interaction_area()

    for cell in i_border.cells:
        is_mouse_over = cell.contains_coordinates(pygame.mouse.get_pos())
        is_mouse_pressed = pygame.mouse.get_pressed()[0]
        if is_mouse_over or cell.is_selected:
            draw_cell_rect(screen, cell, 0)
            if is_mouse_pressed:
                i_border.select_cell(cell)
        else:
            draw_cell_rect(screen, cell, 1)

    # draw border
    pygame.draw.rect(
        screen,
        WHITE,
        i_border.get_rect(), 
        i_border.border_thickness
    )


def handle_mouse(screen):
    mouse_pos = pygame.mouse.get_pos()

    font = pygame.font.SysFont("Arial", 24)
    font_surface = font.render(str(mouse_pos), True, WHITE)
    screen.blit(font_surface, (0,0))

def on_mouse_up():
    i_area = GAME_MANAGER.get_interaction_area()

    if len(i_area.selected_cells) > 0 and not GAME_MANAGER.mimic.is_moving:
        # do mimic stuff
        target_cell = GAME_MANAGER.get_mimic_area_cell_from_interaction_area_cell(
            i_area.selected_cells[-1]
        )
        GAME_MANAGER.mimic.start_moving(target_cell)

    # reset interaction area
    i_area.deselect_all_cells()

def draw_cell_rect(screen, cell, border):
    pygame.draw.rect(
                screen,
                GRAY,
                cell.get_rect(),
                border
            )


run_game()
