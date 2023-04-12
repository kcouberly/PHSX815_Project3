import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#load in output file from Bernoulli.py
data = np.loadtxt('output.txt')
#record number of heads, tails, and total flips
total = len(data)
heads = np.sum(data)
tails = total - heads

print('total flips',total)
print('heads',heads)
print('tails',tails)

#function proportional to likelyhood for the weight parameter
def likelyhood(p,n_H,n_T):
    return((p**n_H) * (1-p)**n_T)

#plotting likelyhood as a function of parameter p
x = np.linspace(0,1,100)
y= []
for i in range(100):
    y.append(likelyhood(x[i],heads,tails))
plt.plot(x,y)
plt.xlabel('bernoulli parameter')
plt.ylabel('relative likelyhood')
plt.title(str(total) + " trials")
plt.show()
    
#minimize function to determine most likely parameter
#negative of likelyhood function
def min_this(p):
    return(-((p**heads) * (1-p)**tails))
#initial guess 0.5
result = minimize(min_this,0.5)
print('best fit p:',result.x[0])
