class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

    def bark(self, num):
        for i in range(num):
            print('Hong', i+1)
