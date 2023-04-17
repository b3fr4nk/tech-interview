# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

# Constraints:

#     -2^31 <= x <= 2^31 - 1

 
# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x: int) -> bool:
    def isPalindrome(self, x: int) -> bool:
        # compare the original string to the reverse note index [::-1] creates the same in reverse
        return str(x) == str(x)[::-1]

    # if x < 0:
    #     return False
    # if x < 10:
    #     return True
    # if x < 100:
    #     digit1 = x % 10
    #     digit2 = x % 100 // 10
        
    #     if digit1 != digit2:
    #         return False
    # elif x < 1000:
    #     digit1 = x % 10
    #     digit3 = x % 1000 // 100

    #     if digit1 != digit3:
    #         return False
    
    # digits = []
    # digits.append(x % 10)
    # place = 2
    # while x // (10**len(digits)) > 0:
    #     digits.append((x % 10 ** place) // (10 ** (place - 1)))
    #     place += 1
    # for i in range(len(digits)//2-1):
    #     print(len(digits)//2-1)
    #     if digits[i] != digits[i-1]:
    #         return False
    # return True

    #     if x < 10:
    #         return True
    #     elif x < 100:
    #         digit1 = x % 10
    #         digit2 = x % 100 // 10
            
    #         if digit1 == digit2:
    #             return True
    #     else:
    #         digit1 = x % 10
    #         digit3 = x % 1000 // 100

    #         if digit1 == digit3:
    #             return True

print(isPalindrome(11))