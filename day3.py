#today i am creating parent class and child class
class Partner:
    def __init__(self,name,email,city):
        self.name=name
        self.email=email
        self.city=city

    def __repr__(self):#this python function every time return print 
        return f"{self.name} ({self.email}) from {self.city}"

class Customer(Partner):
    def __init__(self,name,email,city,discount_percent):# this is parent class method call in child classs
            super().__init__(name,email,city)
            self.discount_percent=discount_percent

    #this is override method
    def __repr__(self):
            return f"{super().__repr__()} {self.discount_percent}% discount"

partner=Partner("arshita","arshitapatel077@gmail.com","Bangluru")
customer=Customer("Jay","jaylim@gmail.com","Bangluru",14)        

print(partner)#othwrwise i am note write this __repy__ that time i am direct not printing i create another function that time print(partner.anotherfunction name)
print(customer)