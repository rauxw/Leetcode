def isAnagram(string,target):

    if len(string) != len(target):
        return False
    
    countString, countTarget = {}, {}

    for i in range(len(string)):
        countString[string[i]] = 1 + countString.get(string[i], 0)
        countTarget[target[i]] = 1 + countTarget.get(target[i], 0)
    
    for c in countString:
        if countString[c] != countTarget.get(c,0):
            return False

    return True

print(isAnagram("tar",'rat'))