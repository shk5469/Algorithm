n = int(input())
ball = list(map(int,input().split(" ")))
sub = []
res = 0

ball.sort()

print(ball)
for i in range(n-1):
    res = res + ball[i+1] - ball[i]

res = res + ball[len(ball)-1] - ball[0]

print(res)

