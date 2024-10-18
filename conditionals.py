################ CONDITIONALS #####################


# if elif else
x = int(input("what's x? "))
y  = int(input("what's y? "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
    
    
#or
x = int(input("what's x? "))
y  = int(input("what's y? "))

if x <y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
    
# not equal
x = int(input("what's x? "))
y  = int(input("what's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
    
# and
score = int(input("score: "))
if score >= 90 and score <= 100:
    print("grade A")
elif score >= 80 and score < 90:
    print("grade B")
elif score >= 70 and score < 80:
    print("grade C")
elif score >= 60 and score < 70:
    print("grade D")
else:
    print("grade F")
    
    
#chaining comparison operators

score = int(input("score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



#Modulo 
x = int(input("what's x? "))

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
    
    
#using functions and bools
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
    
#Pythonic expression
def is_even(n):
    return (n % 2 == 0)

main()



#switch
name = input("what's your name? ")

if name == 'harry' or name == 'hermione' or name == 'ron':
    print('goat')
elif name == 'ram':
    print('go0')
else:
    print('lucky person')
    
    
    
#match
name = input("what's your name? ")

match name:
    case 'harry' | 'hermione' | 'ron':
        print('goat')
    case 'ram':
        print('go0')
    case _:
        print('lucky person')

