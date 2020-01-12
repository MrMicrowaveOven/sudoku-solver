from space import Space
from time import sleep

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

    def is_solved(_):
        solved = True
        spaces = _.spaces
        for row in spaces:
            for space in row:
                if not space.value:
                    solved = False
        return solved


    def attempt_to_solve(_):
        while not _.is_solved():
        # for i in range(20):
            _.show_board()
            _.one_round_of_elimination()
            sleep(1)
            print '==========================================================='
        _.show_board()


    def one_round_of_elimination(_):
        spaces = _.spaces
        for i, row in enumerate(spaces):
            for j, space in enumerate(row):
                _.attempt_to_guess_space([i,j])

    def attempt_to_guess_space(_, space_coords):
        _.run_count_elimination(space_coords)
        _.run_area_elimination(space_coords)
        _.get_space(space_coords).solve_check()

    def run_count_elimination(_, space_coords):
        spaces = _.spaces
        space = _.get_space(space_coords)
        if not space.value:
            eliminating_values = _.get_eliminating_values(space_coords)
            space.eliminate_possibles(eliminating_values)

    def run_area_elimination(_, space_coords):
        space = _.get_space(space_coords)
        possibles = space.possibles

        _.run_elimination(space, _.get_hor_spaces(space_coords))
        _.run_elimination(space, _.get_vert_spaces(space_coords))
        _.run_elimination(space, _.get_block_spaces(space_coords))

    def run_elimination(_, space, related_spaces_coords):
        possibles_of_relatives = []
        for related_space_coords in related_spaces_coords:
            related_space = _.get_space(related_space_coords)
            possibles_of_relatives += related_space.possibles

        possibles_of_relatives = list(set(possibles_of_relatives))
        unique_possibles = list(set(space.possibles) - set(possibles_of_relatives))
        if len(unique_possibles) == 1:
            space.fill(unique_possibles[0])

    def get_space(_, space_coords):
        return _.spaces[space_coords[0]][space_coords[1]]

    def fill_space(_, space, value):
        spaces = _.spaces
        space = spaces[space[0]][space[1]]
        space.fill(value)

    def get_eliminating_values(_, space):
        spaces = _.spaces
        eliminating_spaces = _.get_related_spaces(space)
        eliminating_values = []
        for eliminating_space in eliminating_spaces:
            value = spaces[eliminating_space[0]][eliminating_space[1]].value
            if value:
                eliminating_values.append(value)
        return list(set(eliminating_values))


    def get_related_spaces(_, space):
        return _.get_hor_spaces(space) + _.get_vert_spaces(space) + _.get_block_spaces(space)

    def remove_own_space(_, spaces, space):
        spaces.remove(space)
        return spaces

    def get_block_spaces(_, space):
        size = _.size
        block_spaces = []
        block_vert_index = space[0] / 3
        block_hor_index = space[1] / 3
        for i in range(3):
            for j in range(3):
                block_spaces.append([block_vert_index * 3 + i, block_hor_index * 3 + j])
        block_spaces = _.remove_own_space(block_spaces, space)
        return block_spaces

    def get_vert_spaces(_, space):
        size = _.size
        vert_spaces = []
        column_index = space[1]
        for i in range(size):
            vert_spaces.append([i, column_index])
        vert_spaces = _.remove_own_space(vert_spaces, space)
        return vert_spaces

    def get_hor_spaces(_, space):
        size = _.size
        hor_spaces = []
        row_index = space[0]
        for i in range(size):
            hor_spaces.append([row_index, i])
        hor_spaces = _.remove_own_space(hor_spaces, space)
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
