import Cell

class AttackCellWrapper(object):
    def __init__(self, cell):
        self.cell = cell
        self.red_value = 0

    def get_rect(self):
        return self.cell.get_rect()

    def add_color(self):
        self.red_value += 1
        if (self.red_value > 255):
            self.red_value = 0
        return (self.red_value, 0, 0)
    