#Implement a function that reverses a string using iteration...and then recursion!
def reversedString(s):
    stringreversed = ""
    for i in range(len(s)-1, -1, -1):
        stringreversed = stringreversed + s[i]
    return stringreversed

print(reversedString('yoyo mastery'))

    


