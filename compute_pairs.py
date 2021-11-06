from collections import Counter
pile = [3,3,1,2,3,2,1,3,2,3,1,3,3,1,3,1,1,2,2,2] #pile of socks
pair_count = list(Counter(pile).items())
num_pairs = 0
for key, value in pair_count:
    num_pairs += int(value/2)
    print('Color', key, '=', int(value/2), 'pairs and', int(2*(value/2-int(value/2))), 'Odd Socks')
print('total number of pairs = ', num_pairs)