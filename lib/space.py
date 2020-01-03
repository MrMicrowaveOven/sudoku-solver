class Space:
    def __init__(self):
        self.value = None

    def is_filled(self):
        return self.value != None

    def fill(self, value):
        self.value = value

    def empty(self):
        self.value = None
