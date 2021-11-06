import random
from collections import Counter
import matplotlib.pyplot as plt

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
        
print(num_pairs_sum)
    
num_colors = []
for i in range(color):
    num_colors.append((i+1)*3)

print(num_colors)

for i in range(color):
    plt.plot(num_colors, num_pairs_sum) #ploting data points
plt.xlabel("number of colors")
plt.ylabel("number of pairs")
plt.title("number of pairs for each color")
