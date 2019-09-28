#Electrical circuit
#Consider the following electrical circuits. All the resistors are equivalent. 

#Find the equations that link VA, VB, VC and VD. Millmann's theorem might helps you. 
#Write a program that solve these equation to compute the value of these four voltages. 
#What will be the value of point A, B, C and D ?
#Which other Python packages could you have used to solve this problem?

#https://drive.google.com/file/d/1UJoQMAlqkgE3y64AafjxtowPWNrbspt5/view?usp=sharing

'''
Va=(15+Vb+Vc+Vd)/4
Vb=(15+Va+Vd)/3
Vc=(Va+Vd)/3
Vd=(Va+Vb+Vc)/4
'''
import numpy as np
A = np.array([[-1,1/4,1/4,1/4], [1/3,-1,0,1/3],[1/3,0,-1,1/3],[1/4,1/4,1/4,-1]])
B = np.array([-15/4,-15/3,0,0])
Z = np.linalg.solve(A,B)
print(Z)