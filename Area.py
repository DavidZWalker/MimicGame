import Cell
import random

class Area(object):
    def __init__(self, pos_x, pos_y, width, height, cols, rows):
        self.color = (128, 128, 128)
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.border_thickness = 3
        self.cells = self.__add_cells(cols, rows)
        self.selected_cells = []
        self.rows = rows
        self.cols = cols

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
                cell = Cell.Cell(
                    c * col_width + self.pos_x,
                    r * row_height + self.pos_y,
                    col_width,
                    row_height
                )
                cell.row = r
                cell.column = c
                cells.append(cell)
        
        return cells

    def find_neighbor_cell(self, home_cell, direction):
        if direction == "up":
            if home_cell.row <= 0:
                return None
            return self.__get_cell_at(home_cell.row-1, home_cell.column)
        if direction == "down":
            if home_cell.row >= self.rows:
                return None
            return self.__get_cell_at(home_cell.row+1, home_cell.column)
        if direction == "right":
            if home_cell.column >= self.cols:
                return None
            return self.__get_cell_at(home_cell.row, home_cell.column+1)
        if direction == "left":
            if home_cell.column <= 0:
                return None
            return self.__get_cell_at(home_cell.row, home_cell.column-1)
    
    def __get_cell_at(self, row, col):
        for cell in self.cells:
            if cell.row == row and cell.column == col:
                return cell

    def get_random_cell(self):
        row = random.randint(0, self.rows-1)
        col = random.randint(0, self.cols-1)
        return self.__get_cell_at(row, col)