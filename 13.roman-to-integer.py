#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        temp_num = 0
        temp_letter = ""
        total = 0
        for x in s:
            if x == "I":
                temp_num = 1
                temp_letter = "I"
                total += 1
            elif x == "V":
                if temp_num > 5 or temp_num == 5 or temp_num == 0:
                    temp_num = 5
                    temp_letter = "V"
                    total += 5
                else:
                    new_letter = temp_letter + "V"
                    if new_letter == "IV":
                        total -= 1
                        total += 4
                        temp_num = 0
            elif x == "X":
                if temp_num > 10 or temp_num == 10 or temp_num == 0:
                    temp_num = 10
                    temp_letter = "X"
                    total += 10
                else:
                    new_letter = temp_letter + "X"
                    if new_letter == "IX":
                        total -= 1
                        total += 9
                        temp_num = 0
            elif x == "L":
                if temp_num > 50 or temp_num == 50 or temp_num == 0:
                    temp_num = 50
                    temp_letter = "L"
                    total += 50
                else:
                    new_letter = temp_letter + "L"
                    if new_letter == "XL":
                        total -= 10
                        total += 40
                        temp_num = 0
            elif x == "C":
                if temp_num > 100 or temp_num == 100 or temp_num == 0:
                    temp_num = 100
                    temp_letter = "C"
                    total += 100
                else:
                    new_letter = temp_letter + "C"
                    if new_letter == "XC":
                        total -= 10
                        total += 90
                        temp_num = 0
            elif x == "D":
                if temp_num > 500 or temp_num == 500 or temp_num == 0:
                    temp_num = 500
                    temp_letter = "D"
                    total += 500
                else:
                    new_letter = temp_letter + "D"
                    if new_letter == "CD":
                        total -= 100
                        total += 400
                        temp_num = 0
            else:
                if temp_num > 1000 or temp_num == 1000 or temp_num == 0:
                    temp_num = 1000
                    temp_letter = "M"
                    total += 1000
                else:
                    new_letter = temp_letter + "M"
                    if new_letter == "CM":
                        total -= 100
                        total += 900
                        temp_num = 0

        return total

# @lc code=end

