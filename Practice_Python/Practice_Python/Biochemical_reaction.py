#Biochemical reaction
#In this exercise,  we simulate  an enzymatic reaction involving four chemical species: 
#an enzyme E, a substrate S, a product P and a complex formed by the enzyme and the substrate ES. 
#Two reactions are involved in the process:

#1)The binding between the E and S, which gives ES. This reaction is reversible. 
#The forward reaction constant is k1 and the reverse reaction constant is k−1.

#2)The degradation of ES into E and P. This reaction is not reversible. 
#The forward reaction constant is k2.

#All reactions are modeled by first-order kinetics law.

#Deterministic approach

#Establish the set of 4 differential equations that describe the behavior of the concentration of E, S, P and ES.
#Compute the response of the chemical system over 60 seconds with k1=0.01, k−1=0.001, k2=5 
#and an initial quantity of enzyme E0=10 and substrate S0=1000. Initial concentration of ES and P is 0.
#Plot E, S ES and P as a function of the time. 

#Biochemical reaction
import matplotlib.pyplot as plt
import numpy as np

def reaction(E,S,ES,P,k1=0.01,k2=0.001,k3=5):
  dS = -k1*E*S + k2*ES
  dES= k1*E*S - (k2+k3)*ES
  dE = -k1*E*S + (k2+k3)*ES
  dP = k3*ES
  return dE,dS,dES,dP

number_of_stages = 60001
dt = 0.001
E = np.empty(number_of_stages)
S = np.empty(number_of_stages)
ES = np.empty(number_of_stages)
P = np.empty(number_of_stages)
time = np.arange(0,60.0+dt, dt)

E[0],S[0],ES[0],P[0] = (10.0, 1000.0,0,0)

for i in range(number_of_stages - 1):
  dE,dS,dES,dP = reaction(E[i],S[i],ES[i],P[i])
  E[i+1] = E[i] + dE *dt
  S[i+1] = S[i] + dS *dt
  ES[i+1] = ES[i] + dES *dt
  P[i+1] = P[i] + dP *dt


plt.plot(time, E, c='blue', label="E")
plt.plot(time, S, c='red', label="S")
plt.plot(time, ES, c='purple', label="ES")
plt.plot(time, P, c='green', label="P")

plt.xlabel("Time [s]")
plt.ylabel("Quantity")
plt.title("Deterministic approach")
plt.grid()
plt.legend()
plt.show()