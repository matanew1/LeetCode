 ##############################################################################################
#  A function that converts every roman number to a number in decimal                          #
#  The problem called : "Roman to Integer"                                                     #
#  At : https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/ #
#  Solved by Matan Bardugo                                                                     #
 ##############################################################################################
class Solution(object):
    def romanToInt(self, s):
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        i = len(s)-1
        while i >= 0:
            if  i == len(s)-1:
                number += romans[s[i]]
            else:
                if romans[s[i]] >= romans[s[i+1]]:
                    number += romans[s[i]]
                else:
                    number -= romans[s[i]]
            i -=1
        return number

if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("MMCDXXV"))
