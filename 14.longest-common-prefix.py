#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first_strs = strs[0]
        last_strs = strs[-1]
        for itemA, itemB in zip(first_strs, last_strs):
            if itemA == itemB:
                ans += itemA
            else:
                return ans
        return ans

# @lc code=end

