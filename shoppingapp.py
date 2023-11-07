import json
from kivy.app import App
from kivy.lang import Builder

names_to_prices = [{"name": "Cheese", "price": 12.5}, {"name": "Laptop", "price": 912.95},
                   {"name": "Plant", "price": 4.75}, {"name": "Coffee Machine", "price": 2300.00},
                   {"name": "Guitar", "price": 4399.95}]
name_to_price = {}


class ShoppingAPP(App):
    """Main program for Kivy app for shopping"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_price = {}

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('')
        return self.root

    def add_to_total(self):
        pass

    def reset_total(self):
        pass


ShoppingAPP().run()
