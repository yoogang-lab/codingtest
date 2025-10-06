import sys
sys.setrecursionlimit(10**6)


def letterCombinations(digits: str) -> list[str] :
    def dfs(index, path) :
        if len(path) == len(digits) :
            result.append(path)
            return
        for i in range(index, len(digits)) :
            print( dic[digits[i]])
            for j in dic[digits[i]] :
                # print(j)
                dfs(i + 1, path + j)


    dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    result = []
    dfs(0,"")

    return result

print(letterCombinations("23"))