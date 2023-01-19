t = int(input())
A = [] 
B = []

for i in range(t):
    a, b = map(int, input().split(" "))
    A.append(a)
    B.append(b)

for a, b  in zip(A,B):
    print(a+b)