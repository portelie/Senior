import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50  # 0 - не голодний, 100 - дуже голодний
        self.energy = 50  # 0 - валиться з лап, 100 - заряджений
        self.happiness = 50  # 0 - депресія, 100 - щасливий як ніколи

    def feed(self):
        if self.hunger > 20:
            self.hunger -= 20
            self.happiness += 10
            print(f"{self.name}: \"Заебісь\"")
        else:
            print(f"{self.name}: \"Та я не голодний, відстань зі своєю їжею!\"")

    def play(self):
        if self.energy > 20:
            self.happiness += 20
            self.energy -= 20
            print(f"{self.name}: \"Ура! Граємо!\"")
        else:
            print(f"{self.name}: \"Сука дай поспати.\"")

    def sleep(self):
        self.energy += 30
        self.hunger += 10
        print(f"{self.name}: \"Хррр... Хррр... Найкращий сон!\"")

    def live_day(self):
        self.hunger += random.randint(10, 20)
        self.energy -= random.randint(10, 20)
        self.happiness -= random.randint(5, 15)
        print(f"{self.name}: \"Ще один день у житті...\"")

    def status(self):
        print(f"\n{self.name} ({self.species}):")
        print(f"Голод: {self.hunger}, Енергія: {self.energy}, Щастя: {self.happiness}")

# Тестування
kitty = Pet("Мурчик", "кіт")
for _ in range(3):  # Три дні життя кота
    kitty.status()
    kitty.live_day()
    action = random.choice([kitty.feed, kitty.play, kitty.sleep])
    action()
