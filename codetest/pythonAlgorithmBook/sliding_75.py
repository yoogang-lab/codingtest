import collections

results = []
def maxSlidingWindow(nums,k) :

    window = collections.deque()
    currentMax = float('-inf')

    for i, v, in enumerate(nums) :
        window.append(v)
        if i < k - 1 :
            continue

    if currentMax == float('-inf') :
        currentMax = max(window)
    elif v > currentMax :
        currentMax = v

    results.append(currentMax)

    if currentMax == window.popleft():
        currentMax = float('-inf')

    return  results

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(results)