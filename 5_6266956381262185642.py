class orang:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def intro(self):
        print("Name : ", self.name, "\nAge : ", self.age, "\nGender : ",
              self.gender)

class perkenalan(orang):
    def __init__(self, namef, age, gender):
        super().__init__(namef, age, gender)
andi = perkenalan("Cici", 21, "Female")
andi.intro()

