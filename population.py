import numpy as np
import matplotlib.pyplot as plt
n = np.array(range(5 * 52))
dt = 1/7
t = n * dt
k = 0.1
K = 1000
m = 10
P_0vals = [300, 600, 900, 1200, 1500]
P = []
for j in range(5):
    P.append(P_0vals[j])

    for i in range(1, 5*52):
        P_i = dt*(((k * P[i-1]) * (1 - (P[i-1] / K))) - m) + P[i-1]
        P.append(P_i)
    
    fig, ax = plt.subplots()
    ax.plot(t, P, label = f'P_0 = {P_0vals[j]}')
    ax.legend()
    

plt.show()