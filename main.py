import numpy as np
import matplotlib.pyplot as plt

## This is analysis of pandemic expansion base on one paper () research ().
## We try to use simplify version formular of this paper as main simulation formular
## In order to apply this formular,we have to take some assumption
## ... (more explanation)
# Set up the time interval
dt = 0.1
# Set up the time domain
t = np.arange(0,10,dt) # From 0 to 10 with time interval 0.1(s)

# set up initial condition for P, S, I,and R
# P is number of total population
# S is ...
# I is number of infectious people
# R is number of recovered people

P = 10000
S = np.zeros_like(t)
I = np.zeros_like(t)
R = np.zeros_like(t)

I[0] = 1
R[0] = 0
S[0] = P - I[0]

a = 0.001  # Infectious coefficient of susceptible people
b = 0.00005  # Infectious coefficient of recovered people
g = 0.02   # Recover rate of infectious people
# process.....

for i in range(1,len(t)):
    S[i] = S[i-1] - a*dt*I[i-1]*S[i-1]
    I[i] = I[i-1] + a*dt*I[i-1]*S[i-1] + b*dt*I[i-1]*R[i-1] - g*I[i-1]
    R[i] = R[i-1] + g*I[i-1] - b*dt*I[i-1]*R[i-1]

fig = plt.figure(figsize=(10,10))
plt.plot(t, S, "b-", label="susceptible")
plt.plot(t, I, "r-", label="infectious")
plt.plot(t, R, "g-", label="recovered")
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.grid()
plt.title("Pandemic expansion model with a, b, g is {0}, {1}, {2}".format(a, b, g))
plt.legend()
plt.show()






