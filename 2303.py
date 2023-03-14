from itertools import combinations

N = int(input())
n, m = [], []
for i in range(N):
    n.append(list(combinations(list(map(int, input().split(" "))), 3)))
    for j in range(len(n[i])):
        n[i][j] = sum(n[i][j]) % 10
    n[i] = max(n[i])

for i in range(len(n)):
    if n[i] == max(n):
        m.append(i+1)
        
print(max(m))
