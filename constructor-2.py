class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f'Hi I am {self.name}')


john = Person("John smith")
john.greet()
bob = Person("Bob smith")
bob.greet()