def dp(weight, count, weights, costs):
    preline, curline = [0] * (weight + 1), [0] * (weight + 1)
    for i in range(count):
        for j in range(weight + 1):
            if weights[i] <= j:
                curline[j] = max(preline[j], costs[i] + preline[j - weights[i]])
        preline = curline[:]
    return curline[weight]
count=5
weight=10
costs=[6,3,5,4,6]
weights=[2,2,6,5,4]
print(dp(weight,count,weights,costs))