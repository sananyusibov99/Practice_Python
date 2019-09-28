#In this exercise, we will calculates a derivative. 
#For that purpose, keep in mind the mathematical definition of a derivative is

# dfdx=lim(δx→0)((f(x+δx)−f(x))/δx)

#Write a script that calculate the derivative of f(x)=x2 on 101 points between 0 and 10 for δx=10−2. 
#Plot the error curve (i.e. expected value – computed value) over the 101 points.
#Do the same for different values of different values on δx ranging from 10−2 to 10−14.
#How does the error vary with the δx?


#Derivative
import matplotlib.pyplot as plt

i=0
i_values = []
delta = 0.01
y = []
while i<=100:
    y.append(((i+delta)**2 - i**2)/delta)
    i_values.append(i)
    i = i+delta
plt.plot(i_values, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()