import math


T = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(T):
    Ns, Ls = input().split()

    N = int(Ns)
    L = int(Ls)

    S = input().split()

    order = [0] * (L + 1)
    minEl = S[0]
    minPos = 0
    for i in range(1,L):
        if int(S[i]) < minEl:
            minEl = S[i]
            minPos = i

    # if i == L - 1:

    

    firstNum = math.gcd(int(S[0]), int(S[1]))
    order.append(int(S[0])//firstNum)
    order.append(firstNum)
    order.append(int(S[1])//firstNum)

    for i in range(2, L):
        order.append(int(S[i]) // order[i])

    d = set(order)

    cypher = sorted(d)

    result = ''
    for i in range(L+1):
        result += alpha[cypher.index(order[i])]

    print("Case #" + str(t + 1) + ": " + result)