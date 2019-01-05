# Why do we create function
# to avoid repetation of code

# What is function scope
# function scope is betwen its start line and end line

# How to create function that accepts 2 parameters
def add(aa,bb):
    print(aa+bb)
    
# How to call a functions
# add()

# How to pass parameter to function
add(4,7)


# Return value from function
def add1(aa,bb):
    c = aa+bb
    return c

# Return value from function & print
def add2(aa,bb):
    c = aa+bb
    return c

# 1 way
result = add2(2,3)
print(result)

# 2 way
print(add2(2,3))

# Assign value returned by function to variable
def add3(aa,bb):
    c = aa+bb
    return c
    
result = add3(4,3)
print(result)


# Return String from function and print
def add4(aa,bb):
    space=' '
    c = aa + space + bb
    return c
    
result = add4('prajakta','bhosale')
print(result)

# Pass array of string as parameter to function
# Return Array of string from function and print
# Inside function add new item inside functions
def add5(listOfFruits):
    listOfFruits.append('chicku')
    return listOfFruits
    
add5_result = add5(['orange','apple','banana'])
print(add5_result)


# Pass object as parameter to function
# Return object from function and print
# Inside function add new key to object
def add6(object):
    object['idiot'] = 'yes'
    # object.idiot = 'yes'
    return object
    
add6_result = add6({'name' : 'prajakta' , 'age' : 90, 'dob' : 'nov'})
print(add6_result)


# Pass array of object as parameter to function
# Return array of object from function and print
# Inside array of object push/add new object



# How to pass parameters to function

# How to write formula inside function

# Assign computed value from function to variable & prints
 
# Create a function that will calculate area of One square
# Then function should accept two parameters width and height and calculate area
# Then print
# def areaOfsquare(aa):
#     area = aa*aa
#     return area

# resultOfOneSquare = areaOfsquare(2)
# print(resultOfOneSquare)

# Create function that will calculate area of 5 squares
# Then function should accept areas for 5 squares like calculateAreas(22 , 9 , 56, 12 ,3)
# Then print 
# Then output should be 3854


# def calculateAreas(a,b,c,d,e):
#     a1 = areaOfsquare(a) #22 
#     b1 = areaOfsquare(b) #9
#     c1 = areaOfsquare(c) #56
#     d1 = areaOfsquare(d) #12
#     e1 = areaOfsquare(e) #3
#     result = a1+b1+c1+d1+e1
#     return result

# calculateAreas_Result = calculateAreas(22 , 9 , 56, 12 ,3)

# print(calculateAreas_Result)





















#  def add(aa,bb):
#     print(aa+bb)
    
# add(4,7);


# def addstring(aa,bb):
#     print(aa + ' '+bb)
    
# addstring('Vijay','Prajakta') 


# def updateJson(aa):
#     aa['name'] = 'prajakta'
#     aa['age'] = 20
#     print(aa)
    
# updateJson({ "name" : 'vijay',"age": '40'})


# Myinfo = { "name" : 'vijay',"age": '40'}





# print(Myinfo['name'] + 'pawar')
