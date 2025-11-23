# bakery.py

class Item:
    def __init__(self, name: str, price: float, emoji: str):
        self.name = name
        self.price = price
        self.emoji = emoji

class Bakery:
    def __init__(self):
        self.sweets = [
            Item(name="Chocolate Cake", price=4.0, emoji="🍫"),
            Item(name="Vanilla Cake", price=3.5, emoji="🍰"),
            Item(name="Red Velvet", price=5.0, emoji="❤️")
        ]

        self.coffees = [
            Item(name="Espresso", price=2.0, emoji="☕"),
            Item(name="Latte", price=2.5, emoji="🥛"),
            Item(name="Cappuccino", price=2.5, emoji="🍮")
        ]

        self.mojitos = [
            Item(name="Classic Mojito", price=3.0, emoji="🍸"),
            Item(name="Strawberry Mojito", price=3.5, emoji="🍓"),
            Item(name="Mint Mojito", price=3.0, emoji="🌿")
        ]

    def get_items(self, category: str):
        if category == "Sweets":
            return self.sweets
        elif category == "Coffee":
            return self.coffees
        elif category == "Mojitos":
            return self.mojitos
        else:
            return []
