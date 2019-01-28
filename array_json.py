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

  # Q4 - How many people are not married
counter = 0      
for item in patient:
    if item['married'] == False:
        counter = counter +1
        
# print(counter) 

# Q6 - How many people work at boston_dynamics
many = 0
for item in patient:
    if item['company'] == 'boston_dynamics':
        many = many +1

# print(many)


# Q5 - A person With first name Brok was detected with coriander_allergy on 1 jan 2019 with severity level
# As medium.So please update his allergies records with this newly detected

for item in patient:
     if item['first_name'] == 'Brok':
        # print(item)
        h = item['allergies']
        print(h)
        
        item['allergies'] = [{'name':'coriander_allergy','severity_level':'medium','detection_date':'2019-01-01'}]
        
        print(item['allergies'])
      
  Q7 - Get total salary of person whose first_name is Antonella,Jonathan,Dulcea
total_salary = 0
for item in patient:
    if item['first_name'] == 'Antonella':
        print('Antonella')
        print(item['salary'])
        total_salary = total_salary + item['salary']
        
    if item['first_name'] == 'Jonathan':
        print('Jonathan')
        print(item['salary'])
        total_salary = total_salary + item['salary']
  
    if item['first_name'] == 'Dulcea':
        print('Dulcea')
        print(item['salary'])
        total_salary = total_salary + item['salary']
  
    
print('Total Salary')
print(total_salary)    
      
        
# Q7  Using If condition - Get total salary of person whose first_name is Antonella,Jonathan,Dulcea
# total_salary = 0
# for item in patient:
#     if item['first_name'] == 'Antonella' :
#         print('Antonella')
#         print(item['salary'])
#         total_salary = total_salary + item['salary']
        
#     if item['first_name'] == 'Jonathan':
#         print('Jonathan')
#         print(item['salary'])
#         total_salary = total_salary + item['salary']
  
#     if item['first_name'] == 'Dulcea':
#         print('Dulcea')
#         print(item['salary'])
#         total_salary = total_salary + item['salary']
  
    
# print('Total Salary')
# print(total_salary)    


#Q7.1 - Using If / Or operator- Get total salary of person whose first_name is Antonella,Jonathan,Dulcea
# total_salary = 0
# for item in patient:
#     if item['first_name'] == 'Antonella' or item['first_name'] == 'Jonathan' or item['first_name'] == 'Dulcea' :
#         print(item['first_name'])
#         print(item['salary'])
#         total_salary = total_salary + item['salary']
    
# print('Total Salary')
# print(total_salary)    

# Q7.2 - Using in operator - Get total salary of person whose first_name is Antonella,Jonathan,Dulcea

total_salary = 0
people = ['Antonella', 'Jonathan' ,'Dulcea']
for item in patient:
    if item['first_name'] in people:
        print(item['first_name'])
        print(item['salary'])
        total_salary = total_salary + item['salary']
        
print('Total Salary')
print(total_salary) 

# Q8 - Increment salary of person by 10,000 whose email id is gjotham13@nature.com

for item in patient:
    if item['email'] == 'gjotham13@nature.com':
        print(item['salary'])
        h = item['salary'] + 10000
        print(h)

# Q9 - What is total asset count 0f Barbabra

count = 0
for item in patient:
    if item['first_name'] == 'Barbabra':
        assets_of_barbara = item['assets']
        for a_o_b in assets_of_barbara:
            count = count + 1
print(count)
# Q10 - What is total worth of Emmery
#  count = 0
# for item in patient:
#     if item['first_name'] == 'Emmery':
#         assets_of_Emmery = item['assets']
#         for a_o_e in assets_of_Emmery:
#             count = count + 1

# print(count)

# Q11 - Mr Edward Purchased New villa of worth 30,000 .So please update his assets list 

# for item in patient:
#      if item['first_name'] == 'Edward':
#      print(item)
#         h = item['assets']
#         print(h)
        
#         item['assets'] = [{'name':'New villa','worth':30000}]
        
#         print(item['assets'])
  
# Q12 -  Which phd person is having highest salary

highest_salary = 0
for item in patient:
    if item['Qualification'] == 'phd':
        if item['salary'] > highest_salary :
            highest_salary = item['salary']

print(highest_salary)
