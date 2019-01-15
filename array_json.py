from data import *

# ACCESS JSON
yo = {'name' : 'vijsy' , 'age' : 23 , 'schools' : ['primary','secondary']}

# set
yo['age'] = 44
print(yo)

# get
h = yo['age']
print(h)

# ACCESS ARRAY
fruitsList = ["apple", "banana", "cherry"]
def myFormula(yooo):
    add = yooo + ' hello '
    subract = add + ' hiee '
    khanaKhaKeJana = subract + ' hmm '
    print(khanaKhaKeJana)
    
for item in fruitsList:
    myFormula(item)


# SOLVE QUESTIONS FROM DOCUMENT
counter  = 0
for item in patients:
    if item['gender'] == "Male":
        counter = counter + 1
        
print(counter)        
        

from data import *

patientList = patient

# Q1 - get data of person whose first name is Georgie
# for item in patient:
#      if item['first_name'] =='Georgie':
#         # print(item)
         
# Q2 -  how many people have phd as highest qualification
# counter = 0
# for item in patient:
#     if item['Qualification'] == 'phd':
#         counter = counter +1
        
# print(counter)  

# Q3 - update salary to 60000 whose first name is Feodor 

for sawt34tr4 in patient:
    if sawt34tr4['first_name'] == 'Feodor':
        sawt34tr4['salary'] = 60000
        print(sawt34tr4)

        
        


