n, m = map(int, input().split(" "))
a = []
N, M = 0, 0
for i in range(n):
    a.append(list(input()))
for i in a:
    if "X" not in i:
        N += 1
for i in range(m):
    for j in range(n):
        if a[j][i] == "X":
            c = True
            break
        else:
            c = False
    if not c:
        M += 1

print(max([N,M]))