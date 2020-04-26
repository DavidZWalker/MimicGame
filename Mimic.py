class Mimic(object):
    def __init__(self, starting_cell):
        self.width = 20
        self.height = 20
        self.move_speed = 0
        self.max_speed = 20
        self.is_moving = False
        self.cell = starting_cell
        self.__center_in_cell()
        self.target_cell = self.cell

    def get_rect(self):
        return [
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        ]

    def start_moving(self, target):
        self.is_moving = True
        self.target_cell = target

    def move(self):
        relative_center = self.target_cell.get_relative_center(self.width, self.height)
        remaining_x = relative_center[0] - self.pos_x
        remaining_y = relative_center[1] - self.pos_y
        if remaining_x > 100 or remaining_y > 100:
            self.__calc_move_speed("up")
        else: 
            self.__calc_move_speed("down")
        if remaining_x > 0:
            self.pos_x += self.move_speed
        if remaining_y > 0:
            self.pos_y += self.move_speed
        if remaining_x < 0:
            self.pos_x -= self.move_speed
        if remaining_y < 0:
            self.pos_y -= self.move_speed
        if remaining_x <= 1 and remaining_x >= -1 and remaining_y <= 1 and remaining_y >= -1:
            self.stop_moving()

    def stop_moving(self):
        self.is_moving = False
        self.cell = self.target_cell
        self.move_speed = 0
        self.__center_in_cell()

    def __calc_move_speed(self, direction="up"):
        if direction == "up":
            if self.move_speed == 0:
                self.move_speed = 1
            elif self.move_speed == 1:
                self.move_speed = 2
            else:
                self.move_speed = min(self.move_speed*self.move_speed, self.max_speed)
        else:
            if self.move_speed > 2:
                self.move_speed /= 2
            else:
                self.move_speed = max(self.move_speed-1, 1)


    def __center_in_cell(self):
        self.pos_x = self.cell.get_center()[0] - self.width/2
        self.pos_y = self.cell.get_center()[1] - self.height/2