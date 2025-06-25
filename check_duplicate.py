# Brute Force Method
def brute_force(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Optimized Version
def optimized_version(nums):
    numSet = set()
    for i in nums:
        if nums[i] in numSet:
            return True
        numSet.add(i)
    return False

print(optimized_version([1,2,3,3]))