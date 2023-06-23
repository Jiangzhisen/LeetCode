#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        length_str = len(strNum)
        slice_str = strNum[length_str::-1]
        if strNum == slice_str:
            ans = True
        else:
            ans = False
        return ans

# @lc code=end

