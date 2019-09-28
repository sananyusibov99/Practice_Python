#In this exercise we will write a script to estimate π by computing the area of the unitary circle. 
#Two approaches will be compared.

# Integration with trapezoid method

#Split the [−1;1] range into n stripes (see figure below). 
#Then, calculate the area occupied by the circle in each stripe and by considering it as a trapezoid. 
#Finally, add them together in order to obtain the area of the circle.
#Do the same for different values of n, such as 10, 100, 1000 ... 
#What is the impact of n on the accuracy of the estimation of π?


# Integration with a stochastic method:

#Write a script that draws randomly npoints in a square of size 2 centered on (0,0). 
#Then, use the equation of the unitary circle, i.e. x2+y2=1 to count the number of point inside the circle. 
#Finally, use this value to estimate the area of the circle.
#Do the same for different values of n, such as 10, 100, 1000 ... 
#What is the impact of n on the accuracy of the estimation of π?


#evaluation of pi using stochastic method
import random
import math

count_inside = 0
for count in range(0,10000):
  d=math.hypot(random.random(), random.random())
  if d<1:
    count_inside+=1
print(4.0*count_inside/count)


#evaluation of pi using trapezoid
import math
area_total=0
area=0

radius=1
number_of_stripes=1000
b1=radius
b2=0
h=0
for i in range(1, number_of_stripes):
  h=(radius*i/number_of_stripes)
  b2=math.sqrt(radius**2 - h**2)
  area = ((b1+b2)/2)*(radius/number_of_stripes)
  area_total += area
  b1=b2
  
print(f"Area is {4*area_total}")

