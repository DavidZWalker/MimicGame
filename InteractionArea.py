import Area

class InteractionArea(Area.Area):

    def get_cell_at(self, coordinates):
        cell = next(filter(lambda x: x.contains_coordinates(coordinates), self.cells))

        return cell

    def select_cell(self, cell):
        cell.select()
        if cell not in self.selected_cells:
            self.selected_cells.append(cell)
    
    def deselect_all_cells(self):
        for cell in self.cells:
            cell.deselect()
        self.selected_cells.clear()    