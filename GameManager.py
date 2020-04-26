import InteractionArea, MimicArea, Mimic

class GameManager(object):
    def __init__(self, game_area):
        width = 100
        height = 100
        cols = 3
        rows = 3
        self.interaction_area = InteractionArea.InteractionArea(
            (game_area[0]/2)-(width/2), 
            game_area[1]-height-20, 
            width, 
            height, 
            cols, 
            rows)
        
        self.mimic_area = MimicArea.MimicArea(
            (game_area[0]/2)-(450/2), 
            20, 
            450, 
            450, 
            3, 
            3
        )

        self.mimic = Mimic.Mimic(self.mimic_area.cells[0])
    
    def get_interaction_area(self):
        return self.interaction_area

    def get_mimic_area(self):
        return self.mimic_area

    def get_mimic_area_cell_from_interaction_area_cell(self, i_cell):
        i = 0
        for c in self.interaction_area.cells:
            if c == i_cell:
                break
            i += 1
        
        return self.mimic_area.cells[i]
        