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

class contactbook:
    def __init__(self):
        self.partners=[]

    def add(self,partner):
        self.partners.append(partner)

    def remove(self,email):
        for partner in self.partners:
            if partner.email == email:
                self.partners.remove(partner)
                return True
            return False

    def find_by_city(self,city):
        result=[]
        for partner in self.partners:
            if partner.city == city:
               result.append(partner)
        return result

    def find_by_email(self,email):
        for partner in self.partners:
            if partner.email == email:
                return partner
        return None
    def report(self):
        print(f"Total partner:{len(self.partners)}")
        for partner in self.partners:
            print(self.partner)

    def __len__(self):
        return len(self.partners)

    def __iter__(self):
        return iter(self.partners)
    

partner1=partner("arshita","arshpatel077@gmail.com","Bangluru",123000)
partner2=partner("Jay","jay23@gmail.com","Ahemdabad",345212)
partner3=partner("Rutvi","Rut32@gmail.com","Bangluru",983451)

customer1=customer("jay","jaylim@gmail.com","Bangluru",69098,10)

print(partner1)
print(customer1)

book = contactbook()
book.add(partner1)
book.add(customer1)
book.add(partner2)

print("Total:",len(book))

print("find by city")
for person in book.find_by_city("Bangluru"):
    print(person)
