nums = [2, 0, 11, 15, 8, 1, 7]  # Input list of numbers
target = 9 # Target value

#Solution 1: Brute Force Loop x2. O(n2)- Slow Runtime
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution() # Create an instance of the Solution class
result = solution.twoSum(nums, target) # Call the twoSum method to find the indices of the two numbers that add up to the target
print("Indices of the two numbers:", result) # Print the result


#Solution 2: Brute Force 2
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j])


#Solution 3: Dictionary
class Solution:
    def twoSum(self, nums, target):
        seenDict = {}
        i = 0                               #Set up the index i to be 0, why?
        while i < len(nums):
            num = nums[i]
            diff = target -  num            # Iterate through the array and get it's current element aswell as it's complement (difference).
            if diff in seenDict:            # If the difference exists in the hash map.
                return [i, seenDict[diff]]  # Return it's index as well as a it's complement index.
            seenDict[num] = i               # Otherwise, add the current element to the dictionary (hash map) along with it's current index.
            i += 1                          # Move to next element?


#Solution 4: Dictionary (Works) Neetcode
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, n in enumerate(nums):          # For index and nums, get the value and the index at the same time.
            diff = target - n
            if diff in seen:            # Does the dictionary contain, the number we'd need to add to our current number, to equal target.
                return([seen[diff], i]) # Return th evalue in the seen dictionary of the rarget. Second value is i.
            seen[n] = i
        return


#Solution 5: 
class Solution:
    def twoSum(self, nums, target):
        dictionary = {}

        for i in range(len(nums)):
            dictionary[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dictionary and dictionary[diff] != i:
                return[i, dictionary[diff]]
            
#Solution 6:
class Solution(object):
    def twoSum(self, nums, target):
        dict_of_seen_values = {}

        for index, currentNumber in enumerate(nums):
            required_number = target - currentNumber

            if required_number in dict_of_seen_values:
                return [index, dict_of_seen_values[required_number]]
            else:
                dict_of_seen_values[currentNumber] = index

