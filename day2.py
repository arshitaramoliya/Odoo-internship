class Partner:
    def __init__(self,name,email,city,credit_limit):
        self.name=name
        self.email=email
        self.city=city
        self.credit_limit=credit_limit

    def describe(self):
        return {self.name,self.email,self.city,self.credit_limit}

  

#create 8 object
Partners = [

            Partner("Arshita","arshitapatel077@gmail.com","Delhi",500000),
            Partner("Jay","jaylim@gmail.com","Ahemdabad",300000),
            Partner("Monika","monika@gmail.com","Delhi",100000),
            Partner("Dixt","dixit23@gmail.com","Rajkot",240000),
            Partner("Drushiv","drushiv56@gmail.com","Rajkot",500000),
            Partner("Rahi","rahi98@gmail.com","pune",2000000),
            Partner("Krishna","krishna34@gmail.com","Pune",560000),
            Partner("Ram","ram78@gmail.com","Rajkot",340000),

           ]  
#1.give a name stay in pune city
def partners_in_city(Partners,city): 
    result = []

    for p in Partners:
        if p.city == city:
            result.append(p)
    return result

pune_partner = partners_in_city(Partners, "pune")

print("Partners in Pune:")

for p in pune_partner:
    print("-", p.name)

#2.calculate total credit

def total_credit (Partner):
    total=0

    for p in Partner:
        total=total+p.credit_limit

    return total
total = total_credit(Partners)
print("Total credit rupees:",total)

#3.which partner is credit biggest
def big_credit(Partner):
    biggest=Partners[0]
    for p in Partner:
        if p.credit_limit>biggest.credit_limit:
            biggest = p

    return biggest
biggest = big_credit(Partners)
print("biggest customer:",biggest.name,biggest.credit_limit)
        
    
