############ FILE I/O ####################

#list

names = []

for _ in range(3):
    
    name = input("what's your name? ")
    names.append(name)
    
for name in sorted(names):
    print(f'hello,{name}')



#open
name = input("what's your name? ")

file = open('names.txt', 'w')
file.write(name)
file.close()


#with
name = input("what's your name? ")

with open('names.txt', 'w') as file:
    file.write(name)
