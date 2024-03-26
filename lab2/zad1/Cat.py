import Animal


class Cat(Animal):

    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return print("Moew, Moew!")
