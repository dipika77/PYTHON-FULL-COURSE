######################## LOOPS #######################

#while loop
n = 5
while n > 0:
    print(n)
    n -= 1
print('blastoff!')


#for loop
for i in range(3):
    print('hello')
    
    
#Validating input
while True:
    n = int(input("what's n? "))
    if n < 0:
        break
    
for _ in range(n):
    print('hello')
    
    
#Iteration with list
students = ['ram', 'shyam', 'hari']
print(students[0])
for student in students:
    print(student)
    
    
#len
students = ['ram', 'shyam', 'hari']
for i in range(len(students)):
    print(i, students[i])   #here is is used to denote the indent of numbers
 
 
#Dictionary
students= {
    'ram': 'gryffindor', 
    'shyam': 'gryffindor', 
    'hari': 'slytherin'
    }

for student in students:
    print(student)  #it will only print keys(students name)
    print(students[student])  #it will print values(students house)
    print(student, students[student]) #it will print both keys and values




#list of dictionaries
students= [
    {'name': 'ram', 'house': 'gryffindor'}, 
    {'name': 'shyam', 'house': 'gryffindor'}, 
    {'name': 'hari', 'house': 'slytherin'}
    ]

for student in students:
    print(student)  #it will only print keys(students name)
    print(student['name'], student['house'], sep='')  #it will print values(students house)
    
    
    
#Nested loops
def main():
    print_square(3)
    
def print_square(size):
    
    # for each row in square
    for i in range(size):
        
        #for each column in square
        for j in range(size):
            
            #print a '#'
            print('#', end='')
        print()

   

    