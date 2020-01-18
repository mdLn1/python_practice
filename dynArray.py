N = 2
queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1]
]

def dynamicArray(n, q):
    seqList = [[] for x in range(n)]
    lastAnswer = 0
    answers = []
    for arr in q:
        queryType, x, y = arr
        if queryType == 1:
            seqList[((x ^ lastAnswer) % n)].append(y)
        else:
            seq = seqList[((x ^ lastAnswer) % n)]
            lastAnswer = seq[y % len(seq)]
            answers.append(lastAnswer)
    return answers
    

print(dynamicArray(N, queries))