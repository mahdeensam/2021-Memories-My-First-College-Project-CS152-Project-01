'''Mahdeen Ahmed Khan Sameer 
02/14/2022
CS 152 A 
Lab 01'''

print( 'version 1' )
print( 'sum', 42 + 21 + 5 )
print( 'avg', (42 + 21 + 5) / 3 )



#Defining a Function

def myFunction(a, b, c):
    print('sum', a + b + c )
myFunction( 4, 5, 6)

#Version2
print( 'version 2' )
print( 'sum', 42 + 21 + 5 )
print( 'avg', (42 + 21 + 5) // 3 )

#Version3
print( 'version 3' )
print( 'sum', 42 + 21 + 5.0 )
print( 'avg', (42 + 21 + 5) // 3.0 )

#Version4
a = 42
b = 21
c = 5
print( 'sum', (a + b + c))
print( 'avg', (a+ b+ c)/3.0 )

#Version5

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
print( 'sum', (a + b + c))

#Version6

def stats( a, b, c):
    print( 'sum', (a + b + c))
    print( 'avg', (a+ b+ c)/3.0 )
stats(42, 21, 5)





