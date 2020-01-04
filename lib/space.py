class Space:
    def __init__(_):
        _.value = None
        _.possibles = range(1,10)

    def eliminate_possibles(_, possibles_to_eliminate):
        possibles = _.possibles
        if type(possibles_to_eliminate).__name__ == 'int':
            possibles.remove(possibles_to_eliminate)
        else:
            possibles = list(set(possibles) - set(possibles_to_eliminate))
        _.possibles = possibles
        _.solve_check()

    def intersect_possibles(_, possibles_to_intersect):
        possibles = _.possibles
        _.possibles = [possible for possible in possibles if possible in possibles_to_intersect]
        _.solve_check()

    def solve_check(_):
        possibles = _.possibles
        # if len(possibles) == 0:
            # raise CustomError('No possibles')
        if len(possibles) == 1 and not _.value:
            _.value = possibles[0]
        if _.value:
            _.possibles = [_.value]

    def is_filled(_):
        return _.value != None

    def fill(_, value):
        _.value = value

    def empty(_):
        _.value = None
