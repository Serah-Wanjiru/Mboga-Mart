class Add_item:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price
    def item_name(self,p_name):
        self.name=p_name
    def item_quantity(self,n_quantity):
        self.quantity=n_quantity
    def item_price(self,n_price):
        self.price=n_price
    def __str__(self):
        return f"{self.name},{self.quantity},{self.price}"
# //Add_item
i1=Add_item("cabagges",45,5000)
# //Add_item
print(i1)