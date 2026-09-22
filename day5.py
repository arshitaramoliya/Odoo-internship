class patner:
    def __init__(self,name,email,city):
        self.name=name
        self.email=email
        self.city=city
    #readable for programmer
    def __repr__(self):
        return f"({self.name}, 's email id id ,{self.email}, she/he staying in , {self.city})"
    
#this is function use for true and false ans 
#Normally Python objects ko memory location se compare karta. But __eq__ bolta hai: agar email same hai, to partner same maan lo.

    def __eq__(self,other):
        return self.city==other.city

    def __iter__(self):
        return iter(self.partner)
#this is use for length in list
    def __len__(self):
        return len(self.Data)
    
    #generally ae list me use kar skte ho
    #readable for user
    def __str__(self):
        return f"{self.name} from {self.city}"

    
    
patner1=patner("Arshita","ars@gmail.com","Bangluru")
patner2=patner("Jay","jay23@gmail.com","Ahemdabad")
patner3=patner("Rutvi","Rut32@gmail.com","Bangluru")

Data=[patner1,patner2,patner3]
print(Data)
#lenth of a list
print(len(Data))

#this function use for debuging __repr__

print(repr(patner1)) 
print(str(patner1))

#this is function use for true and false ans 
#Normally Python objects ko memory location se compare karta. But __eq__ bolta hai: agar email same hai, to partner same maan lo.

print(" same city patner: ",patner1==patner3)




