#Factorial
#Write a function that takes an integer as input and that returns
#its factorial (n!). Try two ways to implement these functions:

#One with dynamic evaluations using  eval() function.
#One with a recursive function call.


#Factorial using recursion
def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print(f"The factorial of {num} is {fact(num)}")


#Factorial using eval()
num = int(input("Enter a number: "))
factorial = "1"

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(2,num + 1):
       factorial = factorial + "*" + str(i)
   print(factorial)
   print(f"The factorial of {num} is {eval(factorial)}")

