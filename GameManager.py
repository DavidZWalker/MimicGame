import MimicArea, Mimic

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

        self.mimic = Mimic.Mimic(self.mimic_area.cells[0])

    def get_neighbor_cell(self, direction):
        current_cell = self.mimic.cell
        return self.mimic_area.find_neighbor_cell(current_cell, direction)


        