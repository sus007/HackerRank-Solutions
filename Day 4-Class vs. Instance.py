class Person(object):
    def __init__(self, initalAge):
        if initalAge >= 0:
            self.age = initalAge #Here self.age represents that the variable "age" is actually an instance variable but not a local one.
        else:
            self.age = 0
            print "Age is not valid, setting age to 0.."

#Adding a method to increaxe the age by 1
    def yearPasses(self): #Here passing self to the method definition represents that "yearPasses" is an instance method.
        self.age += 1       
#Defining a method to test the supplied age    
    def amIOld(self):
        if self.age < 13:
    	    print "You are young.."  
        elif self.age >= 13 and self.age < 18:
            print "You are a teenager.."
        else:
            print "You are old.."
'''
#Instantiating the Class "Person" by supplying a parameter i.e initialAge
res = Person(9)

#Accessing the instance method of "yearPasses()" of the res instance
res.yearPasses()

#Accessing the instance method of "amIOld()" of the res instance
res.amIOld()          
'''
t = int(raw_input("Enter an integer: "))
for i in range(0, t):
    age = int(raw_input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()        
    p.amIOld()
    print("")            
            