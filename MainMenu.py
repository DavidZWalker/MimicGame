import Button

class MainMenu(object):
    def __init__(self, menu_dimensions):
        width = menu_dimensions[0]
        self.start_button = Button.Button()
        self.start_button.set_location(width/2-self.start_button.width/2, 300)
        self.start_button.set_text("Start")
        self.is_open = True