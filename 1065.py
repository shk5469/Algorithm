n = int(input())
sub = 0
res = 0

for i in range(1,n+1):
    x = []
    while i !=0:
        x.append(i % 10)
        i = int(i / 10)
    if len(x) < 3:
        res += 1
    else:
        sub = x[1] - x[0]
        for j in range(1,len(x)-1):
            if x[j+1] == x[j] + sub:
                continue
            else:
                sub = 'x'
        if sub != 'x':
            res += 1
print(res)