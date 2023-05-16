# //login
class Login:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
    def input_username(self,new_username):
        self.username=new_username
        
    
    
    def input_password(self, new_password):
        self.password = new_password
        
    def update_email(self, new_email):
        self.email = new_email
    def __str__(self):
        return f"{self.username},{self.password},{self.email}"
# //Login
l1=Login("mashrima vee","mash3345","mashrima@gmail.com")
# //login
print(l1)  