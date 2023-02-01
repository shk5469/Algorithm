n, m = map(int, input().split(" "))
j = int(input())
r = m
l = 1
res = 0
for i in range(j):
    d = int(input())
    if d > r:
       res = res + (d-r)
       r = d
       l = d - m + 1
    elif d < l:
       res = res + (l-d)
       l = d
       r = d + m - 1

print(res)