class Partner:
    def __init__(self,name,email,city,credit_limit):
        self.name=name
        self.email=email
        self.city=city
        self.credit_limit=credit_limit

    #for printing - use repr mothod
    # def describe(self):
    #     return {self.name,self.email,self.city,self.credit_limit}

    def __repr__(self):
        return f"({self.name}, city={self.city})"

    def __lt__(self, other):
        return self.name < other.name

#1.give a name stay in pune city
def partners_in_city(partners,city): 
    city = city.lower()
    result = []

    for p in partners:
        if p.city.lower() == city:
            result.append(p)
    return result

#2.calculate total credit

def total_credit (Partner):
    total=0

    for p in Partner:
        total=total+p.credit_limit

    # for i in range(len(Partner)):
    #     p = partner[i]
    #     total+= p.credit_limit
        
    return total
#3.which partner is credit biggest
def big_credit(partner):
    biggest=partners[0]
    for p in partner:
        if p.credit_limit>biggest.credit_limit:
            biggest = p

    return biggest

#---------

#create 8 object
partners = [

            Partner("Arshita","arshitapatel077@gmail.com","Delhi",500000),
            Partner("Jay","jaylim@gmail.com","Ahemdabad",300000),
            Partner("Monika","monika@gmail.com","Delhi",100000),
            Partner("Dixt","dixit23@gmail.com","Rajkot",240000),
            Partner("Drushiv","drushiv56@gmail.com","Rajkot",500000),
            Partner("Rahi","rahi98@gmail.com","pune",2000000),
            Partner("Krishna","krishna34@gmail.com","Pune",560000),
            Partner("Ram","ram78@gmail.com","Rajkot",340000),

           ]  

# partners = [53,5343,5,7,32]

print("All My parters: ",partners)

partners.sort(reverse=False)

print("Sorted All My parters: ",partners)
# print(partners[0])

# pune_partner = partners_in_city(partners, "pune")

# print("Partners in Pune:", pune_partner)

# # for p in pune_partner:
# #     print("-", p.name)


# total = total_credit(partners)
# print("Total credit rupees:",total)


# biggest = big_credit(partners)
# print("biggest customer:",biggest.name,biggest.credit_limit)


        
    
