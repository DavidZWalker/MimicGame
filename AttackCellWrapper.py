import Cell

class AttackCellWrapper(object):
    def __init__(self, cell):
        self.cell = cell
        self.red_value = 0
        self.attack_complete = False

    def get_rect(self):
        return [
            self.cell.pos_x,
            self.cell.pos_y,
            self.cell.width,
            self.cell.height
        ]

    def add_color(self, amount):
        self.red_value += amount
        if (self.red_value > 255):
            self.red_value = 0
            self.attack_complete = True
        return (self.red_value, 0, 0)
    