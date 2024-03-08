class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(self.name + " is barking!")


dog1 = Dog("Bob", 10, "black")
dog2 = Dog("Alice", 8, "silver")
dog3 = Dog("Puszek", 5, "dun")
dog1.sound()
dog2.sound()
dog3.sound()

