import random

# Initialize matrix 
matrix = [] 
# Initialize a list
primes = []
for possiblePrime in range(2, 100):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
      
    if isPrime:
        primes.append(possiblePrime)


R=3
C=3
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(random.choice(primes))) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
