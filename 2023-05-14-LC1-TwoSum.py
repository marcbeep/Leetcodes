# Use a hash table to store the values of the input array and corresponding indices

# Time complexity: O(n) where n is the length of the input array nums
# We iterate over each element of the input array once and perform a constant time operation
# Worst case, there are no two elements that add up to the target sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the elements and their indices
        num_dict = {}

        # Loop through elements of input array
        for i, num in enumerate(nums):
            # Calculate if the complement (target - num)
            complement = target - num

            # Check of it exists in the dictionary
            if complement in num_dict:
                # If exists, return the indices of the two numbers
                return [num_dict[complement], i]
            
            # If it doesn't exist, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no two numbers add up to the target sum, return an empty list
        return []
        
# Tests
nums = [2, 7, 11, 15]
target = 9
# expected output [0, 1]

solution = Solution()
output = solution.twoSum(nums, target)
print(output)