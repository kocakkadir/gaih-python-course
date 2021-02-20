import random


matrix = [] 

primes = []
for possiblePrime in range(2, 100):
    
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
      
    if isPrime:
        primes.append(possiblePrime)


R=3
C=3
for i in range(R):          
    a =[] 
    for j in range(C):       
         a.append(int(random.choice(primes))) 
    matrix.append(a) 
  

for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
