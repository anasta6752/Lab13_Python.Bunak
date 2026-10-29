import fruit_module

fruit = fruit_module.Fruit("Apple", 150, "red")

print("Вид фрукта:", fruit.get_kind())
print("Маса фрукта:", fruit.get_mass())
print("Колір фрукта:", fruit.get_color())

fruit.set_kind("Pear")
fruit.set_mass(180)
fruit.set_color("green")

print("\nПісля зміни властивостей:")
print("Вид фрукта:", fruit.get_kind())
print("Маса фрукта:", fruit.get_mass())
print("Колір фрукта:", fruit.get_color())