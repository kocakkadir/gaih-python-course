def prime_first(number):

  isPrime = True

  if number == 0 or number == 1:
    isPrime = False

  for num in range(2, number):
    if number % num == 0:
      isPrime = False
      
  if isPrime:
    print(number)

def prime_second(number):

  isPrime = True
  for num in range(500, number):
    if number % num == 0:
      isPrime = False
      
  if isPrime:
    print(number)
  

for i in range(0,1000):
  if 0 <= i <= 500:
    prime_f(i)
  elif 500 < i <= 1000:
    prime_second(i)
