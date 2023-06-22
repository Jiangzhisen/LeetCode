#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        startNum1 = 0
        startNum2 = 0
        ans = []
        status = 0
        for num in nums:
            for num1 in nums:
                if startNum1 != startNum2:
                    if num + num1 == target:
                        ans.append(startNum1)
                        ans.append(startNum2)
                        status = 1
                        break
                    else:
                        startNum2 += 1
                        continue
                else:
                    startNum2 += 1
                    continue
            if status == 1:
                break
            startNum1 += 1
            startNum2 = 0
        return ans
# @lc code=end

