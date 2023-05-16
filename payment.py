#  //payment
class Payments:
    def __init__(self,customer,amount,phoneNumber):
        self.customer=customer
        self.amount=amount
        self.phoneNumber=phoneNumber
        #updating customers name in the payment 
    def update_customer(self, new_customer):
        self.customer = new_customer
        #updating amounts in the payment list 
    def update_amount(self, new_amount):
        self.amount = new_amount
        #updating phone Numbers in the payment list
    def update_phoneNumber(self, new_phoneNumber):
        self.phoneNumber= new_phoneNumber
    def __str__(self):
       return f"{self.customer}-{self.amount}-{self.phoneNumber}"

# //Payments
p2=Payments("Julius nyerere",1000,"07453233737")
print(p2)
# //Inventory class
class Inventory:
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price=price
        self.action=action
#updating stock
    def new_stock_levels(self,new_product):
        self.product_name=new_product
# updating stock quanity
    def Quantity_products(self,new_quantity):
        self.quantity=new_quantity
# updating prices
    def pricing(self, new_price):
        self.price=new_price
    def update_action(self,needed_action):
       self.action=needed_action
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"

#//Inventory class
i1 = Inventory("Apple", 100,"sh.500", "add")

# //Inventory
print(i1)