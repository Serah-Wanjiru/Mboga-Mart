# Product class
class OurProducts:
    def __init__(self, name, price, quantity, description, category):
        self.name = name  # Set the product name
        self.price = price  # Set the product price
        self.quantity = quantity  # Set the product quantity
        self.description = description  # Set the product description
        self.category = category  # Set the product category
    
    def update_price(self, new_price):
        self.price = new_price  # Update the product price
    
    def update_quantity(self, new_quantity, new_description):
        self.quantity = new_quantity  # Update the product quantity
        self.description = new_description  # Update the product description
    
    def update_description(self, new_description):
        self.description = new_description  # Update the product description
    
    def update_category(self, new_category):
        self.category = new_category  # Update the product category
    
    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}, {self.description}, {self.category}"

# Create an instance of the product
p1 = OurProducts("Apple", 0.50, 100, "Fresh red apples", "Fruit")
    
# Print the product details
print(p1)