from space import Space
class Board:
    NUMBER_RANGE = range(1,10)

    def __init__(self, size = 9):
        self.size = size
        spaces = [0] * size
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Space())
            spaces[i] = row
        self.spaces = spaces


    def attempt_to_solve(self):
        return True

    def attempt_to_guess_space(self, space_coords):
        spaces = self.spaces
        space = self.get_space(space_coords)
        if not space.value:
            eliminating_values = self.get_eliminating_values(space_coords)
            space.eliminate_possibles(eliminating_values)

    def get_space(self, space_coords):
        return self.spaces[space_coords[0]][space_coords[1]]

    def fill_space(self, space, value):
        spaces = self.spaces
        space = spaces[space[0]][space[1]]
        space.fill(value)

    def get_eliminating_values(self, space):
        spaces = self.spaces
        eliminating_spaces = self.get_eliminating_spaces(space)
        eliminating_values = []
        for eliminating_space in eliminating_spaces:
            value = spaces[eliminating_space[0]][eliminating_space[1]].value
            if value:
                eliminating_values.append(value)
        return list(set(eliminating_values))

    def get_eliminating_spaces(self, space):
        return self.get_hor_spaces(space) + self.get_vert_spaces(space) + self.get_block_spaces(space)

    def get_block_spaces(self, space):
        size = self.size
        block_spaces = []
        block_vert_index = space[0] / 3
        block_hor_index = space[1] / 3
        for i in range(3):
            for j in range(3):
                block_spaces.append([block_vert_index * 3 + i, block_hor_index * 3 + j])
        return block_spaces

    def get_vert_spaces(self, space):
        size = self.size
        vert_spaces = []
        column_index = space[1]
        for i in range(size):
            vert_spaces.append([i, column_index])
        return vert_spaces

    def get_hor_spaces(self, space):
        size = self.size
        hor_spaces = []
        row_index = space[0]
        for i in range(size):
            hor_spaces.append([row_index, i])
        return hor_spaces

    def show_board(self):
        spaces = self.spaces
        size = self.size
        print '  0 1 2 3 4 5 6 7 8'
        print ' ' + '-' * (size * 2 + 1)
        for i, row in enumerate(spaces):
            row_string = str(i) + '|'
            for j, space in enumerate(row):
                if space.is_filled():
                    row_string += str(space.value)
                else:
                    row_string += ' '
                if j % 3 == 2:
                    row_string += '|'
                else:
                    row_string += ' '
            print row_string
            if i % 3 == 2:
                print ' ' + '-' * (size * 2 + 1)
