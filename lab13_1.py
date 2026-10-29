
class Apple:
    def __init__(self, diameter, mass, color):
        self.diameter = float(diameter)
        self.mass = float(mass)
        self.color = str(color)

    def set_diameter(self, diameter):
        self.diameter = float(diameter)

    def set_mass(self, mass):
        self.mass = float(mass)

    def set_color(self, color):
        self.color = str(color)


apple = Apple(3, 7, "white")

print("Колір яблука:", apple.color)
print("Діаметр яблука:", apple.diameter)
print("Маса яблука:", apple.mass)

apple.set_diameter(12.2)
apple.set_mass(150)
apple.set_color("yellow")

print("Новий діаметр:", apple.diameter)
print("Нова маса:", apple.mass)
print("Новий колір:", apple.color)
