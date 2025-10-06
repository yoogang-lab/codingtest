import collections

def minWindow(s, t) :
    need = collections.Counter(t) # char갯수를 셈 예_ BANANA -> Counter({'a': 3, 'n': 2, 'b': 1})
    missing = len(t) # 찾을 문자열의 갯수
    left = start = end = 0

    #오른쪽 포인터 이동
    for right, char in enumerate(s, 1) :
        missing -= need[char] > 0
        need[char] -= 1 #필요한 알파벳 개수 감소시킴

    #필요 문자가 0이면  왼쪽 포인터 이동판단
        if missing == 0 :
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not end or right - left <= end - start : #포인터 이동 왼쪽
                start, end = left,right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]

S = "ADOBECODEBANC"
T = "ABC"

print(minWindow(S,T))