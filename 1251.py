w = input()
r = []
for i in range(1, len(w) - 1):
    for j in range(i + 1, len(w)):
        n = w[:i]
        n1 = w[i:j]
        n2 = w[j:]

        n = n[::-1]
        n1 = n1[::-1]
        n2 = n2[::-1]

        r.append("".join(n + n1 + n2))
r.sort()
print(r[0])