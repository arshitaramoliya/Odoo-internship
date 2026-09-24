class partner:
    def __init__(self,name,email,city,credit_limit):
        self.name=name
        self.email=email
        self.city=city
        self.credit_limit=credit_limit

    def __repr__(self):
        return f"({self.name},{self.email},{self.city},{self.credit_limit})"

class customer(partner):
    def __init__(self, name, email, city, credit_limit,discount_percent):
        super().__init__(name, email, city, credit_limit)
        self.discount_percent = discount_percent

    def __repr__(self):
        return  f"{super().__repr__()},{self.discount_percent} % discount"

    

partner1=partner("arshita","arshpatel077@gmail.com","Bangluru",123000)
patner2=partner("Jay","jay23@gmail.com","Ahemdabad",345212)
patner3=partner("Rutvi","Rut32@gmail.com","Bangluru",983451)

customer1=customer("jay","jaylim@gmail.com","Bangluru",69098,10)

print(partner1)
print(customer1)

len(contact_book)

for partner in contact_book:
    print(partner)