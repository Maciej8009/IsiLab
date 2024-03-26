from Animal import Animal


class Dog(Animal):

    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        # super().sound()
        return print("Woof, Woof!")


dog1 = Dog("Bob", 20, "male", "male")
dog1.sound()
