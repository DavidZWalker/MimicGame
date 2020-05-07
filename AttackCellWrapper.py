import Cell

class AttackCellWrapper(object):
    def __init__(self, cell):
        self.cell = cell
        self.red_value = 0
        self.green_value = 0
        self.blue_value = 0
        self.progression = 0.0
        self.attack_complete = False
        self.is_deadly = False
        self.color = (self.red_value, self.green_value, self.blue_value)
        self.progression_step = 2

    def get_rect(self):
        return [
            self.cell.pos_x,
            self.cell.pos_y,
            self.cell.width,
            self.cell.height
        ]

    def add_color(self):
        self.progression += self.progression_step
        self.red_value = (self.progression/100) * 255
        if self.progression < 75:
            self.green_value = (self.progression/100) * 255
            self.blue_value = (self.progression/100) * 255
        elif self.progression < 90:
            self.green_value = 0
            self.blue_value = 0
        else:
            self.is_deadly = True

        if (self.progression >= 100):
            self.attack_complete = True
            self.is_deadly = False

        return (
            min(self.red_value, 255),
            min(self.green_value, 255),
            min(self.blue_value, 255)
        )
    