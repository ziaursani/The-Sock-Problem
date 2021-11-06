import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

times = 100
color = int(18/3)
sock = 20
sim = []
for i in range(times):
    sim.append([])
    for j in range(color):
        sim[i].append([])
        for k in range(sock):
            sim[i][j].append(random.randint(1, (j+1)*3))

num_pairs = []
for i in range(times):
    num_pairs.append([])
    for j in range(color):
        num_pairs[i].append(0)
        for key, value in list(Counter(sim[i][j]).items()):
            num_pairs[i][j] += int(value/2)

num_pairs_sum = []
for j in range(color):
    num_pairs_sum.append(0)
    for i in range(times):
        num_pairs_sum[j] += num_pairs[i][j]
        
num_pairs_sum = np.array(num_pairs_sum).reshape(-1, 1)
    
num_colors = []
for i in range(color):
    num_colors.append((i+1)*3)

num_colors = np.array(num_colors).reshape(-1, 1)

model = LinearRegression().fit(num_colors, num_pairs_sum)

print('intercept:', model.intercept_[0])

print('slope:', model.coef_[0])

#number of pairs at n=30
num_pairs_at_30 = model.intercept_[0]+model.coef_[0]*30

print('number of pairs at n = 30:', num_pairs_at_30[0])
