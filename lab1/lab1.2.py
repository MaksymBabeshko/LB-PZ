inventory = {
    "молоток": 10,
    "викрутка": 3,
    "дриль": 2,
    "пилка": 7
}

def update_inventory(tool, quantity):
    if tool in inventory:
        inventory[tool] += quantity
    else:
        inventory[tool] = quantity

# Приклади
update_inventory("ключ", 4)
update_inventory("викрутка", -1)

print("Оновлений склад інструментів:")
print(inventory)

low_stock = [tool for tool, qty in inventory.items() if qty < 5]
print("Інструменти з кількістю менше 5:")
print(low_stock)
