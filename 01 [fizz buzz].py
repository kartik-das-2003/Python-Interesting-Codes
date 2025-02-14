print("Fizz_Buzz Play")
import random
n=int(random.randint(0,100))
print("Given Value Of 'n' is:",n)
for i in range(n):
    if(i%3==0 and i%5==0 ):
        print(i," = Fizz_Buzz")
    if(i%3==0):
        print(i," = Fizz")
    if(i%5==0):
        print(i," = Buzz")
    else:
        print(i)            
