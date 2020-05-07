import MimicArea, Mimic, AttackController, MusicController
import random

class GameManager(object):
    def __init__(self, game_area):
        width = 500
        height = 500
        cols = 3
        rows = 3
        
        self.mimic_area = MimicArea.MimicArea(
            (game_area[0]/2)-(width/2),
            (game_area[1]/2)-(height/2),
            width,
            height,
            rows,
            cols
        )

        self.music_controller = MusicController.MusicController()
        self.mimic = Mimic.Mimic(self.mimic_area.cells[0])
        self.attack_controller = AttackController.AttackController()
        self.is_game_over = False
        self.is_paused = False
        self.game_active = False

    def get_neighbor_cell(self, direction):
        current_cell = self.mimic.cell
        return self.mimic_area.find_neighbor_cell(current_cell, direction)

    def get_cell_for_attack(self):
        # only get cells that are not currently under attack
        available_cells = list(filter(
            lambda x: x not in self.attack_controller.get_active_cells(),
            self.mimic_area.cells
            ))

        # the cell with the mimic should have a higher chance of being the attacked cell
        mimic_cell = self.mimic.cell
        available_cells.append(mimic_cell)
        available_cells.append(mimic_cell)
        available_cells.append(mimic_cell)

        # choose randomly from the full list
        cell_nr = random.randint(0, len(available_cells)-1)
        return available_cells[cell_nr]
    
    def check_mimic_collisions(self):
        deadly_attacks = list(filter(lambda x: getattr(x, "is_deadly") == True, self.attack_controller.active_attacks))
        for attack in deadly_attacks:
            if self.mimic.cell.get_rect() == attack.get_rect():
                self.is_game_over = True
                self.music_controller.stop_music()

    def start(self):
        self.game_active = True
        self.music_controller.start()

    def __pause(self):
        self.is_paused = True
        self.music_controller.pause()

    def __resume(self):
        self.is_paused = False
        self.music_controller.start()

    def toggle_pause(self):
        if not self.is_game_over:
            if self.is_paused:
                self.__resume()
            else:
                self.__pause()
