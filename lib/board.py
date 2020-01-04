from space import Space
class Board:
    NUMBER_RANGE = range(1,10)

    def __init__(_, prefill_array = None):
        size = 9
        _.size = size
        spaces = [0] * size
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Space())
            spaces[i] = row
        _.spaces = spaces
        if prefill_array:
            _.prefill_board(prefill_array)

    def prefill_board(_, prefill_array):
        for i, row_array in enumerate(prefill_array):
            for j, value in enumerate(row_array):
                space = _.get_space([i,j])
                space.fill(value)


    def attempt_to_solve(_):
        return True

    def attempt_to_guess_space(_, space_coords):
        spaces = _.spaces
        space = _.get_space(space_coords)
        if not space.value:
            eliminating_values = _.get_eliminating_values(space_coords)
            space.eliminate_possibles(eliminating_values)

    def get_space(_, space_coords):
        return _.spaces[space_coords[0]][space_coords[1]]

    def fill_space(_, space, value):
        spaces = _.spaces
        space = spaces[space[0]][space[1]]
        space.fill(value)

    def get_eliminating_values(_, space):
        spaces = _.spaces
        eliminating_spaces = _.get_eliminating_spaces(space)
        eliminating_values = []
        for eliminating_space in eliminating_spaces:
            value = spaces[eliminating_space[0]][eliminating_space[1]].value
            if value:
                eliminating_values.append(value)
        return list(set(eliminating_values))

    def get_eliminating_spaces(_, space):
        return _.get_hor_spaces(space) + _.get_vert_spaces(space) + _.get_block_spaces(space)

    def get_block_spaces(_, space):
        size = _.size
        block_spaces = []
        block_vert_index = space[0] / 3
        block_hor_index = space[1] / 3
        for i in range(3):
            for j in range(3):
                block_spaces.append([block_vert_index * 3 + i, block_hor_index * 3 + j])
        return block_spaces

    def get_vert_spaces(_, space):
        size = _.size
        vert_spaces = []
        column_index = space[1]
        for i in range(size):
            vert_spaces.append([i, column_index])
        return vert_spaces

    def get_hor_spaces(_, space):
        size = _.size
        hor_spaces = []
        row_index = space[0]
        for i in range(size):
            hor_spaces.append([row_index, i])
        return hor_spaces

    def show_board(_):
        spaces = _.spaces
        size = _.size
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
