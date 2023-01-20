n = int(input())
a = []
b = [0] * n

for i in range(n):
    a.append(list(map(int, input().split(" "))))
    b[i] = [0] * n
for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if a[j][i] == a[k][i]:
                b[k][j] = 1
                b[j][k] = 1

c = []
for i in b:
    c.append(i.count(1))
print(c.index(max(c))+1)

