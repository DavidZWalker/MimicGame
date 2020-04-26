class Cell(object):
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.is_selected = False

    def get_rect(self):
        return [
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        ]

    def get_center(self):
        return (self.pos_x+self.width/2, self.pos_y+self.height/2)

    def get_relative_center(self, relative_width, relative_height):
        return (self.get_center()[0]-relative_width/2, self.get_center()[1]-relative_height/2)

    def contains_coordinates(self, coordinates):
        coord_x = coordinates[0]
        coord_y = coordinates[1]
        contains_x = coord_x > self.pos_x and coord_x <= self.pos_x + self.width
        contains_y = coord_y > self.pos_y and coord_y <= self.pos_y + self.height
        return contains_x and contains_y
    
    def select(self):
        self.is_selected = True

    def deselect(self):
        self.is_selected = False