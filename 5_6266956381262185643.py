class person:
    address = "Enrekang"
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def who(self):
        print("Name : ", self.name)
        print("Age  : ", self.__age)

p1 = person("Cici", 21)
p1.who()
print("Address : ", p1.address)
