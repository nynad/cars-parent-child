class User():
    # hidden variables can only be accessed within the class as a security measure. printing it using a getter function or returning it into a variable and
    # printing the variable is the only way to display it outside of the class 
    __password="123abc"
    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email

    def set_password(self):
        oldpass=input("Please enter the original password: ")
        if oldpass == self.__password:
            newpass=input("Correct, Enter the new password: ")
            self.__password = newpass 
            # to access hidden variables use self. to make it a property  
        else:
            print("Incorrect. Please enter the correct original password.") 
    
    def get_password(self):
        return self.__password 
    # keyword, not a fucntion, no need for brackets

    def display(self):
        print("Here are your account details: \nName:{}\nUsername: {}\nEmail:{}".format(self.name,self.username,self.email))
    

user1=User("Nyna Dammur","nyna_d","nyna@gmail.com")

user1.display() 
Pass1=user1.get_password()
# when returning a value, you must either print it or set a variable for that returned info to be stored in
print(Pass1)

'''
print(user1.email)
print(user1.__password)
'''

class Cars():
    def __init__(self,colour,size,type,brand):
        self.colour=colour
        self.size=size
        self.type=type
        self.brand=brand

    def get_colour(self):
        return self.colour
    
    def repaint(self):
        newcolour=input("What colour do you want to repaint your car with?")
        self.colour=newcolour 
    
    def carshow(self):
        print("This is your new car's properties!:\nColour:{},\nSize:{},\nType:{},\nBrand:{}".format(self.colour,self.size,self.type,self.brand))


class SUV(Cars):
    def __init__(self,colour,size,type,brand,transmission,turbo):
        Cars.__init__(self,colour,size,type,brand)
        self.transmission=transmission
        self.turbo=turbo 

    def carshow(self):
        print("This is your SUV:\nColour:{},\nSize:{},\nType:{},\nBrand:{}\nTransmission:{}\nTurbo:{}".format(self.colour,self.size,self.type,self.brand,self.transmission,self.turbo))

# creating an SUV
suv1=SUV("blue","big","hybrid","honda","low","high")

print(suv1.get_colour())

suv1.carshow()

suv1.repaint()

print(suv1.get_colour())

suv1.carshow()













    


