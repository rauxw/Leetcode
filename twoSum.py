def twoSum(array,target):
    numberMap = {}
    for i in range(len(array)):
        compliment = target - array[i]
        if compliment in numberMap:
            return [numberMap[compliment],i]
        numberMap[array[i]] = i

print(twoSum([2,7,11,15],13))