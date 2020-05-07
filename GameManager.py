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

    def get_neighbor_cell(self, direction):
        current_cell = self.mimic.cell
        return self.mimic_area.find_neighbor_cell(current_cell, direction)

    def get_cell_for_attack(self):
        all_cells = self.mimic_area.cells

        # the cell with the mimic should have a higher chance of being the attacked cell
        mimic_cell = self.mimic.cell
        all_cells.append(mimic_cell)
        all_cells.append(mimic_cell)
        all_cells.append(mimic_cell)

        # choose randomly from the full list
        cell_nr = random.randint(0, len(all_cells)-1)
        return all_cells[cell_nr]
    
    def check_mimic_collisions(self):
        deadly_attacks = list(filter(lambda x: getattr(x, "is_deadly") == True, self.attack_controller.active_attacks))
        for attack in deadly_attacks:
            if self.mimic.cell.get_rect() == attack.get_rect():
                self.is_game_over = True
                self.music_controller.stop_music()

    def start(self):
        self.music_controller.start()

    def __pause(self):
        self.is_paused = True
        self.music_controller.pause()

    def __resume(self):
        self.is_paused = False
        self.music_controller.start()

    def toggle_pause(self):
        if self.is_paused:
            self.__resume()
        else:
            self.__pause()
