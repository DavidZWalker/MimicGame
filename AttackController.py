import AttackCellWrapper

class AttackController(object):
    def __init__(self):
        self.active_attacks = []
        self.attack_interval = 2000
        self.ms_since_last_attack = 0
        self.ms_since_attack_speed_increase = 0

    def get_active_cells(self):
        active_cells = []
        for ac in self.active_attacks:
            active_cells.append(getattr(ac, "cell"))
        return active_cells

    def increase_attack_speed(self):
        self.ms_since_attack_speed_increase = 0
        self.attack_interval = max(250, self.attack_interval-250)

    def attack_cell(self, cell):
        self.ms_since_last_attack = 0
        attack_cell = AttackCellWrapper.AttackCellWrapper(cell)
        self.active_attacks.append(attack_cell)
    
    def update(self, time_since_last_frame):
        self.ms_since_last_attack += time_since_last_frame
        self.active_attacks = list(filter(lambda x: getattr(x, "attack_complete") == False, self.active_attacks))
        self.ms_since_attack_speed_increase += time_since_last_frame
        if self.ms_since_attack_speed_increase > 3000:
            self.increase_attack_speed()
