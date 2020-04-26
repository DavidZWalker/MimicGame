import Cell

class Area(object):
    def __init__(self, pos_x, pos_y, width, height, cols, rows):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.border_thickness = 3
        self.cells = self.__add_cells(cols, rows)
        self.selected_cells = []

    def get_rect(self):
        return [
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        ]

    def __add_cells(self, cols, rows):
        col_width = self.width/cols
        row_height = self.height/rows

        cells = []

        for c in range(cols):
            for r in range(rows):
                cells.append(Cell.Cell(
                    c * col_width + self.pos_x,
                    r * row_height + self.pos_y,
                    col_width,
                    row_height
                ))
        
        return cells