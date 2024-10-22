class Human:

    def __init__(self, name="Human"):
        self.name123 = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print("Names of", self.brand, " passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(passengers)

    for print_passengers()


man1 = Human(name="Jack")
