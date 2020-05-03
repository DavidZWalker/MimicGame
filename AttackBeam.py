class AttackBeam(object):
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.is_moving = False
        self.velocity = 0
        self.max_speed = 100

    def get_rect(self):
        return [
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        ]

    def start_moving(self, direction):
        self.is_moving = True

    def stop_moving(self):
        self.is_moving = False
