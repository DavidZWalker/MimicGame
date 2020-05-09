import sys, pygame
from pygame.locals import QUIT
import GameManager, Engine, MainMenu

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 640
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

MAIN_MENU = MainMenu.MainMenu(WINDOW_SIZE)
GAME_MANAGER = GameManager.GameManager(WINDOW_SIZE)
ENGINE = Engine.Engine()

DRAWABLES = []
MOVABLES = []
ATTACKS = []

SCREEN = pygame.display.set_mode((0, 0))

def initialize_game():
    # init game engine and game manager
    global SCREEN
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("A game")
    SCREEN = pygame.display.set_mode(WINDOW_SIZE)
    show_main_menu()

def start_game():
    global GAME_MANAGER
    global SCREEN
    GAME_MANAGER = GameManager.GameManager(WINDOW_SIZE)
    DRAWABLES.clear()
    MOVABLES.clear()
    ATTACKS.clear()
    for cell in GAME_MANAGER.mimic_area.cells:
        DRAWABLES.append(cell)
    DRAWABLES.append(GAME_MANAGER.mimic)
    MOVABLES.append(GAME_MANAGER.mimic)
    GAME_MANAGER.start()
    run_game_loop()

def run_game_loop():
    # game loop
    while GAME_MANAGER.game_active:
        ATTACKS.clear()
        SCREEN.fill((0, 0, 0))
        handle_pygame_events()

        # draw stuff
        if not GAME_MANAGER.is_game_over and not GAME_MANAGER.is_paused:
            do_attack()
            move_movables()
            draw()
            GAME_MANAGER.check_mimic_collisions()
            update_points()
        elif GAME_MANAGER.is_paused:
            draw()
            show_pause_screen()
        else:
            show_main_menu(GAME_MANAGER.points)

        if not GAME_MANAGER.is_paused and not GAME_MANAGER.is_game_over:
            # update the screen
            pygame.display.update()

def handle_pygame_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                on_arrow_key_pressed("left")
            elif event.key == pygame.K_RIGHT:
                on_arrow_key_pressed("right")
            elif event.key == pygame.K_UP:
                on_arrow_key_pressed("up")
            elif event.key == pygame.K_DOWN:
                on_arrow_key_pressed("down")
            elif event.key == pygame.K_ESCAPE:
                GAME_MANAGER.toggle_pause()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def update_points():
    points_text = pygame.font.SysFont('Arial', 36)
    text = points_text.render(str(GAME_MANAGER.points), False, WHITE)
    text_rect = text.get_rect(center=(100,100))
    SCREEN.blit(text, text_rect)

def handle_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu_mouse_down()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def draw():
    for attack in ATTACKS:
        pygame.draw.rect(
            SCREEN,
            attack.add_color(),
            attack.get_rect(),
            0
        )

    for drawable in DRAWABLES:
        pygame.draw.rect(
        SCREEN,
        drawable.color,
        drawable.get_rect(),
        drawable.border_width
    )

def show_pause_screen():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(128)

    paused_text = pygame.font.SysFont('Arial', 84)
    text = paused_text.render("PAUSED", False, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    overlay.blit(text, text_rect)

    SCREEN.blit(overlay, (0, 0))
    pygame.display.update()

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
    delta_time = ENGINE.get_delta_time()
    attack_controller.update(delta_time)
    if attack_controller.ms_since_last_attack >= attack_controller.attack_interval:
        attack_controller.attack_cell(GAME_MANAGER.get_cell_for_attack())
    
    for attack in attack_controller.active_attacks:
        ATTACKS.append(attack)

def show_main_menu(points=-1):
    start_button = MAIN_MENU.start_button
    if points >= 0:
        start_button.text = "Retry"
    start_button_font = pygame.font.SysFont('Arial', 42)
    title_font = pygame.font.SysFont("Arial", 84)
    title = title_font.render(MAIN_MENU.title_text, True, WHITE)
    title_rect = title.get_rect(center=(WINDOW_WIDTH/2, 100))
    MAIN_MENU.is_open = True
        
    while MAIN_MENU.is_open:
        handle_menu_events()

        # mouse over effects
        mouse_pos = pygame.mouse.get_pos()
        if start_button.is_inside(mouse_pos):
            start_button.border_width = 0
            start_button.text_color = BLACK
        else:
            start_button.border_width = 2
            start_button.text_color = WHITE

        text = start_button_font.render(start_button.text, True, start_button.text_color)
        text_rect = text.get_rect(center=(start_button.pos[0]+start_button.width/2, start_button.pos[1]+start_button.height/2))

        # show points
        if (points >= 0):
            MAIN_MENU.title_text = "Game Over"
            points_font = pygame.font.SysFont("Arial", 48)
            points_string = str(points)
            points_text = points_font.render("You achieved {p} points".format(p=points_string), True, WHITE)
            points_rect = points_text.get_rect(center=(MAIN_MENU.start_button.pos[0]+MAIN_MENU.start_button.width/2, WINDOW_HEIGHT-200))
            SCREEN.blit(points_text, points_rect)

        pygame.draw.rect(SCREEN, start_button.color, start_button.get_rect(), start_button.border_width)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(title, title_rect)
        pygame.display.update()

def menu_mouse_down():
    mouse_pos = pygame.mouse.get_pos()
    start_button = MAIN_MENU.start_button
    if start_button.is_inside(mouse_pos):
        MAIN_MENU.is_open = False
        start_game()
      
initialize_game()
