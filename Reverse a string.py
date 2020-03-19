# Implement a function that reverses a string using iteration...and then recursion!
def reversedString(s):
    stringreversed = ""
    for i in range(len(s)-1, -1, -1):
        stringreversed = stringreversed + s[i]
    return stringreversed

def recursionReversed(s):
    if len(s) == 1:
        return s
    return s[-1] + recursionReversed(s[:len(s)-1])

print(recursionReversed('yoyo mastery'))    
print(reversedString('yoyo mastery'))


