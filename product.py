class Product:

    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price

    def __str__(self):
        return f"This is the name: {self.name} and this is the price: ${self.price}"