class Space:
    def __init__(self):
        self.value = None
        self.possibles = range(1,10)

    def eliminate_possibles(self, possibles_to_eliminate):
        possibles = self.possibles
        if type(possibles_to_eliminate).__name__ == 'int':
            possibles.remove(possibles_to_eliminate)
        else:
            possibles = list(set(possibles) - set(possibles_to_eliminate))
        self.possibles = possibles
        self.solve_check()

    def intersect_possibles(self, possibles_to_intersect):
        possibles = self.possibles
        self.possibles = [possible for possible in possibles if possible in possibles_to_intersect]
        self.solve_check()

    def solve_check(self):
        possibles = self.possibles
        if len(possibles) == 1 and not self.value:
            self.value = possibles[0]

    def is_filled(self):
        return self.value != None

    def fill(self, value):
        self.value = value

    def empty(self):
        self.value = None
