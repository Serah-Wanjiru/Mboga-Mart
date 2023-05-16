
#sigup class 
class Sign_up:
    def __init__(self,username,email,phone_no,password,password_confirmation):
        self.username=username
        self.email=email
        self.phone_no=phone_no
        self.password=password
        self.password_confirmation=password_confirmation
    def update_username(self, new_username):
        self.username = new_username
    
    def update_email(self, new_email):
        self.email = new_email
    
    def update_phone_no(self, new_phone_no):
        self.phone_no = new_phone_no
    
    def update_password(self, new_password):
        self.password = new_password
    def update_password_confirmation(self, new_password_confirmation):
        self.password_confirmation = new_password_confirmation
        
    def __str__(self):
       return f"{self.username},{self.email},{self.phone_no},{self.password},{self.password_confirmation} "
# //Sign_up
s1=Sign_up("Serah Mburu","wanjirumburu@gmail.com","0733938932","serah1233","serah1233")
# //sign up
print(s1)




