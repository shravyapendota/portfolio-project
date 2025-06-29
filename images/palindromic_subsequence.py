def subsets(s):
    res = set()
    def backtrack(i, temp):
        if i == len(s):
            sub = ''.join(temp)
            if sub and is_palindrome(sub):
                res.add(sub)
            return

        temp.append(s[i])
        backtrack(i + 1, temp)
        temp.pop()
        backtrack(i + 1, temp)

    backtrack(0, [])
    return len(res)
def is_palindrome(s):
    return s == s[::-1]

s=input()
print(subsets(s))
