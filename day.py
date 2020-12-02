def entriesThatSum(k, m, n):
    """
    Returns the first list of m elements on n array that sums to k

    k the sum to match
    m how many added use thats sums to k
    n the numbers list
    """
    psum = 0
    idx = list(range(m))
    found = False

    while psum != k and idx[0] < len(n) - 1:
        for i in range(idx[m - 1], len(n)):
            psum = sum([n[a] for a in idx])

            if psum == k:
                found = True
            if psum >= k:
                break

            idx[m - 1] = i

        if found == True:
            break

        ret = False
        idx[m - 1] += 1

        for i in range(len(idx) - 1, -1, -1):
            if ret == True:
                idx[i] += 1

            if idx[i] < len(n):
                ret = False
            else:
                idx[i] = idx[i - 1]
                ret = True

    return idx

with open("./input/d1.txt") as f:
    lines = [int(line.rstrip()) for line in f]

lines.sort()    
idx = entriesThatSum(2020, 2, lines)

res = 1
for i in idx:
    res *= lines[i]

print("Product of 2 values that sums to 2020", res)

lines.sort()    
idx = entriesThatSum(2020, 3, lines)

res = 1
for i in idx:
    res *= lines[i]

print("Product of 3 values that sums to 2020", res)
