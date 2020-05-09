class Button(object):
    def __init__(self):
        self.width = 200
        self.height = 75
        self.pos = (0, 0)
        self.color = (255, 255, 255)
        self.border_width = 2
        self.text = ""
        self.text_color = (255, 255, 255)

    def set_location(self, x, y):
        self.pos = (x, y)

    def set_text(self, text):
        self.text = text

    def get_rect(self):
        return [
            self.pos[0],
            self.pos[1],
            self.width,
            self.height
        ]

    def is_inside(self, position):
        x = position[0]
        y = position[1]
        self_x = self.pos[0]
        self_y = self.pos[1]
        return x >= self_x and x <= self_x+self.width and y >= self_y and y <= self_y+self.height
        