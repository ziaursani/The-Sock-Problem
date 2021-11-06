import random
from collections import Counter

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

print(num_pairs)

