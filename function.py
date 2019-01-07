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
def add7(listofperson):
    listofperson.append({'name': 'Saish', 'age' : 4 ,'address' : 'andheri'})
    return listofperson
    
add7_result = add7([{ 'age':26 ,  'name' : 'prajakta', 'address' : 'andheri' , 'medals' : 7 },
    { 'age':30 , 'name' : 'vijay', 'address' : 'borivali' , 'medals' : 2 }])
print(add7_result)

# How to write formula inside function
def add8(cc,dd):
    space = ' '
    ans = cc + space + dd
    return ans
result = add8('saish','pawar')   
print(result)


# Create a function that will calculate area of One square
# Then function should accept one parameters and calculate area
# Then print
def areaOfsquare(aa):
    area = aa*aa
    return area

resultOfOneSquare = areaOfsquare(2)
print(resultOfOneSquare)

# Create function that will calculate area of 5 squares
# Then function should accept areas for 5 squares like calculateAreas(22 , 9 , 56, 12 ,3)
# Then print 
# Then output should be 3854


def calculateAreas(a,b,c,d,e):
    a1 = areaOfsquare(a) #22 
    b1 = areaOfsquare(b) #9
    c1 = areaOfsquare(c) #56
    d1 = areaOfsquare(d) #12
    e1 = areaOfsquare(e) #3
    result = a1+b1+c1+d1+e1
    return result

calculateAreas_Result = calculateAreas(22 , 9 , 56, 12 ,3)

print(calculateAreas_Result)



#  Create a function that will calculate area of One Triangle
#  Then function should accept two parameters base and height and calculate and Then print
def areaOftriangle(aa,bb):
    area = (aa*bb)/2
    return area

resultOfOnetriangle = areaOftriangle(2,5)
print(resultOfOnetriangle)


# Create function that will calculate area of 3 triangles
# Then function should accept areas for 3 triangles
# Eg : calculateAreas({height : 2,base : 3} , {height : 34,base : 9},{height : 1,base : 7})
# Then print
# Then output should be
# def calculateAreasoftriangles({aaa,bbb} , {ccc,ddd} , {eee,fff}):
#     areafirsttriangles = areaOftriangle(aaa,bbb)
#     areasecondtriangles = areaOftriangle(ccc,ddd)
#     areathirdtriangles = areaOftriangle(eee,fff)
#     resultofthreearea = areafirsttriangles + areasecondtriangles + areathirdtriangles
#     return resultofthreearea
    
# calculateareasoftriangles_result = calculateAreasoftriangles({base : 2,height : 3} , {base : 34,height: 9} , {base : 1, height:7})
# print(calculateareasoftriangles_result)


def calculateAreasoftriangles(t1 , t2 ,t3):
    areafirsttriangles = areaOftriangle(t1['base'],t1['height'])
    areasecondtriangles = areaOftriangle(t2['base'],t2['height'])
    areathirdtriangles = areaOftriangle(t3['base'],t3['height'])
    resultofthreearea = areafirsttriangles + areasecondtriangles + areathirdtriangles
    return resultofthreearea
    
triangel1 = {'base' : 2, 'height' : 4}
triangel2 = {'base' : 34, 'height' : 9}
triangel3 = {'base' : 1,'height' : 7}

calculateareasoftriangles_result = calculateAreasoftriangles( triangel1, triangel2, triangel3)
print(calculateareasoftriangles_result)

















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
