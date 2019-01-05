# Why do we create function
# to avoid repetation of code

# What is function scope
# function scope is betwen its start line and end line

# How to create function
def add(aa,bb):
    print(aa+bb)
    
# How to call a functions
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

# Print value returned by function

# Return Integer from function and print

# Return String from function and print

# Return Array from function and print

# Return Object from function and print

# How to pass parameters to function

# How to write formula inside function

# Assign computed value from function to variable & prints
 
# Create a function that will calculate area of One square
# Then function should accept one parameters and calculate area
# Then print
def areaOfsquare(aa):
    area = aa*aa
    return area

resultOfOneSquare = areaOfsquare(2)
print(resultOfOneSquare)

# Create function that will calculate area of 5 squares
# Then function should accept areas for 5 squares like calculateAreasOfSquares(22 , 9 , 56, 12 ,3)
# Then print 
# Then output should be 3854


def calculateAreasOfSquares(a,b,c,d,e):
    a1 = areaOfsquare(a) #22 
    b1 = areaOfsquare(b) #9
    c1 = areaOfsquare(c) #56
    d1 = areaOfsquare(d) #12
    e1 = areaOfsquare(e) #3
    result = a1+b1+c1+d1+e1
    return result

calculateAreasOfSquares_Result = calculateAreasOfSquares(22 , 9 , 56, 12 ,3)

print(calculateAreasOfSquares_Result)





















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
