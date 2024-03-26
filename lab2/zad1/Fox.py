import Animal


class Fox(Animal):

    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return print("What does the fox say????")
