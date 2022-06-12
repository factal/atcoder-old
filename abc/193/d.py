from itertools import product

k = int(input())
t = input()[:4] # i.e. s
a = input()[:4] # i.e. t

nums = [str(i) for i in range(1, 10)]

card_t = dict(zip(nums, [t.count(i) for i in nums]))
card_a = dict(zip(nums, [a.count(i) for i in nums]))

card_all = dict(zip(nums, [k] * 9))
for key, value in card_t.items():
    card_all[key] -= value
for key, value in card_a.items():
    card_all[key] -= value

remains = 9 * k - 8 # include '#' card

comb = []

for takahashi, aoki in product(nums, repeat=2): # find combinations satisfy the condition
    if card_all[takahashi] == 0 or card_all[aoki] == 0:
        continue

    card_t[takahashi] += 1
    card_a[aoki] += 1
    
    score_t = sum([int(key) * (10 ** value) for key, value in card_t.items()])
    score_a = sum([int(key) * (10 ** value) for key, value in card_a.items()])
    
    if score_t > score_a:
        comb.append((takahashi, aoki))
        
    card_t[takahashi] -= 1
    card_a[aoki] -= 1
prob = []

for takahashi, aoki in comb:
    if takahashi == aoki:
        p = (card_all[takahashi] / remains) * ((card_all[takahashi] - 1) / (remains - 1))        
        prob.append(p)
    else:
        p = (card_all[takahashi] / remains) * (card_all[aoki] / (remains - 1))
        prob.append(p)

print(sum(prob))