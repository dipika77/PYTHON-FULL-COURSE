################## LIBRARIES ########################

#import
import random
coin = random.choice(['heads', 'tails'])
print(coin)


#from
from random import choice
coin = choice(['heads', 'tails'])
print(coin)


#randint, shuffle
import random
cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)
    
    
    
#statistics
import statistics
data = [1, 2, 3, 4, 5]
mean = statistics.mean(data)
print(mean)


#command line arguments
import sys
try :
    print('hello, my name is', sys.argv[1])
except IndexError:
    print('hello, my name is Python')


#to print only name
import sys
if(len(sys.argv) < 2):
    print('too few arguments')
elif(len(sys.argv) > 2):
    print('too many arguments')
else:
    print('hello, my name is', sys.argv[1])
    


#sys.exit
import sys
if len(sys.argv) < 2:
    sys.exit('too few arguments')
elif len(sys.argv) > 2:
    sys.exit('too many arguments')
else:
    print('hello, my name is', sys.argv[1])


#Slices
import sys
if len(sys.argv) < 2:
    sys.exit('too few arguments')

for arg in sys.argv[1:]:
    print('hello, my name is', arg)
    
    
#cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex('hello,' + sys.argv[1])   
    
    
    
#APIs, Requests, JSON
 
import json   
import requests
import sys
if len(sys.argv) != 2:
     sys.exit()
response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])  
print(json.dumps(response.json()))
      


#custom libraries

import sys
from sayings import hello
def main():
    hello('world')
    goodbye('world')
    
def hello(name):
    print('hello,', name)

def goodbye(name):
    print('goodbye,', name)

main()