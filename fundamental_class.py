### Fundamental class examples

#libraries
import numpy as np
# Q1
# Given two matrics A and B, calculate inner product of A and B. 
class calculation:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def inner_product(self):
        print(np.dot(self.A, self.B)) # to print the calculation
        return np.dot(self.A, self.B)
    
    def change_argument(self):
        self.A = self.A + self.B
        
        
d = calculation(np.array([2j, 3j]), np.array([2j, 3j]))
d.change_argument() 
d.inner_product() 

#Q2
# convert dog age into human age. 
#Use the rule of 1 year for a doggo equals 7 years for a human being. 
# 1. Example: print Johnny 7 yr old.
# 2. Example: after 2 yrs, dog becomes y yr old.
# 3. change dog's name

class dog_to_human:
    def __init__(self, dog_name, dog_age):
        self.dog_name = dog_name
        self.dog_age = dog_age
              
    def convert(self):
        print(self.dog_name, 7*self.dog_age)
        return 7*self.dog_age
    
    def age_after_years(self, year):
        print(self.dog_age + year)
        return(self.dog_age + year)
    
    def change_name(self, new_name):
        self.dog_name = new_name
        print(self.dog_name, ", New name:",new_name)
        return self.dog_name, new_name
    
dog_to_human("Johnny", 7).age_after_years(2)
dog_to_human("Johnny", 7).change_name("Buddy")


J = dog_to_human("Johnny", 7)
J.change_name("Buddy")
print(J.dog_name)
print(J.dog_age)
    


    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
