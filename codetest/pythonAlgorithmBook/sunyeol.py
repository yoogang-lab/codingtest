result =[]
prevElements =[]
#
# def dfs(elements):
#     if (len(elements) == 0):
#         result.append(prev_elements[:])
#
#     for e in elements:
#         next_elements = elements[:]
#         next_elements.remove(e)
#
#         prev_elements.append(e)
#         dfs(next_elements)
#         prev_elements.pop()
#

#



def dfs(elements) :
    if len(elements) ==0 :
        result.append(prevElements[:])

    for e in elements :
        current = elements[:]
        current.remove(e)

        prevElements.append(e)
        dfs(current)
        prevElements.pop()

dfs([1,2,3])
print(result)