# Create a dictionary that maps each roman numeral to its corresponding value
# Iterate through roman numeral string left to right

# The time complexity is O(n). It iterates through the string once comparing each character with the next. This is linear.
# In worst case, it performs n-1 comparisons as it stops at the last character.
# The dictionary lookup takes constant time.

from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_sum = 0

        # Loop through Roman numeral string
        for i in range(len(s)):
            # If the current Roman numeral char is the last one, add its value to the total sum and exit
            if i == len(s) - 1:
                total_sum += roman_values[s[i]]
                break
            
            # Otherwise, check the value of the current Roman numeral char
            # If value of next is >= current, add value to total_sum
            if roman_values[s[i]] >= roman_values[s[i+1]]:
                total_sum += roman_values[s[i]]
            else:
                # Else subtract current value from total sum
                total_sum -= roman_values[s[i]]

        return total_sum
        
# Tests
s = input("Enter a Roman numeral: ")
# MCMXCIV will output 1994

solution = Solution()
output = solution.romanToInt(s)
print(output)