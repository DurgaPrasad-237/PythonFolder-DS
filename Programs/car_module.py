# car_module.py

class Car:
    def __init__(self, name, price):
        self.name = name  # Property for the car's name
        self.price = price  # Property for the car's price

    def display_info(self):
        """Method to display the car's name and price."""
        return f"The car {self.name} costs ${self.price}."

    def apply_discount(self, discount_percentage):
        """Method to apply a discount to the car's price."""
        discount = self.price * (discount_percentage / 100)
        self.price -= discount
        return f"The price after {discount_percentage}% discount is ${self.price}."
