class Fruit:
    def __init__(self, kind, mass, color):
        self.kind = str(kind)
        self.mass = float(mass)
        self.color = str(color)

    def set_kind(self, kind):
        self.kind = str(kind)

    def set_mass(self, mass):
        self.mass = float(mass)

    def set_color(self, color):
        self.color = str(color)

    def get_kind(self):
        return self.kind

    def get_mass(self):
        return self.mass

    def get_color(self):
        return self.color