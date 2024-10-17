############### MY PYTHON JOURNEY ################

################ FUNCTIONS AND VARIABLES ############

#Ask user for their name
name = input(" what's your name? ")

#Say hello to user
print('Hello,' + name)

#using quotation marks
print("hello, \"friend\" ")

#Using f-string
print(f"hello, {name}")

#removing whitespaces from string
name = name.strip()

#capitalizing user's name
name = name.capitalize()

#capitalizing user's name
name = name.title()

#split user's name into first name and last name
name = input("what's your name? ")
first, last  = name.split(" ")
print(f"hello, {first} ")

#Calculator app
x = int(input("what's x? "))
y = int(input("what's y? "))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


#Defining functions
def hello(to):
    print("hello,", to)
    
name = input(" what's your name? ")
hello(name)