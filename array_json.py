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
        

