################# EXCEPTIONS ####################

#Try Except
try:
    x = int(input("what's x? "))
    print(f'x is {x}')
except ValueError:
    print("x is not an integer")
    
    
#Name error
try:
    x = int(input("what's x? "))
    print(f'x is {x}')
except:
    print("something went wrong")
    
    
#Else
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
else:
     print(f'x is {x}')
     
     
#Reprompting break
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
    
print(f'x is {x}')


#get_int

def main():
    x = get_int()
    print(f'x is {x}')
def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
main()
    
    
#pass
def main(): 
    x = get_int()
    print(f'x is {x}')
    
def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError :
            pass
        
main()