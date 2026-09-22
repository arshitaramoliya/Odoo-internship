#def it means define function
#__init__ thius is special fuction ,and this meaning is pre define function
#__init__ is automatically run when object is create
 
class Partner:
    def __init__(self,name,email,city,phone_number):
        self.name=name
        self.email=email
        self.city=city
        self.phone_number=phone_number
# i am creating new methos because i need one method call and this method give me this object give full informatin that's why i am creating describe name method

    def describe(self):
        return {self.name} ,{self.email},{self.city},{self.phone_number}
#f it means i am writting all varialble in string
#create 3 object
Partner1=Partner("Arshita","arshitapatel077@gmail.com","Bangluru",7016229473)
Partner2=Partner("Simmi","simmi12@gmail.com","Bhuvneshwar",8912673578)
Partner3=Partner("Rutvi","rutvilim@gmail.com","Rajkot",9812673456)

Partner1.name
print(Partner1.name)
print(Partner1.describe())

