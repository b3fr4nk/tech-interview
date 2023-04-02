class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0 #how many times a character can repeat
        output = 0
        for r in range(len(s)):
            """
            if the substring is not in the dictionary increase the number of characters checked at a time
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
                """
                There are two cases if s[r] in seen:
                case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                case2: s[r] is not inside the current window, we can keep increase the window
                """
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output