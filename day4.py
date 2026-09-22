class Student:
    
    def __init__(self,name,grade):
       self.name= name
       self.__grade= grade #double underscore limit access. --- this is encapsulation concept
       #double underscore limit access   
    #def get_grade(self):
       #   return self.__grade  #u are alredy define encapsulation attribute but this atribute only access u can declare this get method then after this method declate othrwise u can see error
    def __repr__(self):
        return f"{self.name},{self.__grade}"
    
student1=Student('Arshita','A')
student2=Student('Jay','A++')
print(student1.name)
#print(student1.get_grade())
print(student1.__repr__())


#inheritance example
class patner:
    def greeting(self):
        return " Welcome , valued partner"
    
class custemer(patner):
    def greeting(self):
        return super().greeting()+" -you are a register custemer"

class prefercustomer(custemer):
    def greeting(self):
        return super().greeting()+" -you have prefer custemer"


person = prefercustomer()
#print(prefercustomer.greeting(). #error show because class direct call nhi hoga object chahiae
print(person.greeting())
print(prefercustomer.__mro__)


