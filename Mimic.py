import math

class Mimic(object):
    def __init__(self, starting_cell):
        self.color = (255, 255, 255)
        self.border_width = 0
        self.width = 20
        self.height = 20
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.max_speed = 30
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
        dist_delta = abs(math.sqrt(math.pow(remaining_x, 2) + math.pow(remaining_y, 2)))
        move_dir = self.__get_move_dir(remaining_x, remaining_y)
        self.__calc_move_speed(move_dir, dist_delta)
        self.pos_x += self.horizontal_velocity
        self.pos_y += self.vertical_velocity

        if self.horizontal_velocity == 0 and self.vertical_velocity == 0:
            self.stop_moving()
        

    def stop_moving(self):
        self.is_moving = False
        self.cell = self.target_cell
        self.__center_in_cell()

    def __calc_move_speed(self, move_dir, delta):
        accelerate = delta >= 100
        decelerate = delta < 30

        if "right" in move_dir:
            self.horizontal_velocity = self.__calc_velocity(accelerate, decelerate, "h")
        elif "left" in move_dir:
            self.horizontal_velocity = self.__calc_velocity(accelerate, decelerate, "h") * -1
        
        if "down" in move_dir:
            self.vertical_velocity = self.__calc_velocity(accelerate, decelerate, "v")
        elif "up" in move_dir:
            self.vertical_velocity = self.__calc_velocity(accelerate, decelerate, "v") * -1

    def __calc_velocity(self, accelerate, decelerate, direction):
        if direction == "h":
            current_velocity = abs(self.horizontal_velocity)
        else:
            current_velocity = abs(self.vertical_velocity)

        next_velocity = current_velocity
        if accelerate:
            next_velocity = min(math.pow(current_velocity, 3), self.max_speed)
            if next_velocity == current_velocity:
                next_velocity += 1
        elif decelerate:
            if current_velocity < 2:
                next_velocity = max(current_velocity - 0.5, 0)
            else:
                next_velocity = math.sqrt(current_velocity)
        
        return next_velocity
        
    def __get_move_dir(self, remaining_x, remaining_y):
        move_dir = ""
        if remaining_x > 0:
            move_dir += "right"
        elif remaining_x < 0:
            move_dir += "left"
        
        if remaining_y > 0:
            move_dir += "down"
        elif remaining_y < 0:
            move_dir += "up"
        
        return move_dir

    def __center_in_cell(self):
        self.pos_x = self.cell.get_center()[0] - self.width/2
        self.pos_y = self.cell.get_center()[1] - self.height/2