def twoSum(n, t):
    def twoSum(n, t, 4):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[j] == t - n[i]:
                return [i, j]
