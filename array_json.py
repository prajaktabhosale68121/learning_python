from data import *

# JSON operations
yo = {'name' : 'vijsy' , 'age' : 23 , 'schools' : ['primary','secondary']}

# set
yo['age'] = 44
print(yo)

# get
h = yo['age']
print(h)

# solve questions
counter  = 0
for item in patients:
    if item['gender'] == "Male":
        counter = counter + 1
        
print(counter)        
        

