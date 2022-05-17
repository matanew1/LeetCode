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
        print("start at iteration -->",i)
        while i >= 0:
            if  i == len(s)-1:
                number += romans[s[i]]
            else:
                if romans[s[i]] >= romans[s[i+1]]:
                    number += romans[s[i]]
                else:
                    number -= romans[s[i]]
            i -=1
            print("num:",number)

        return number

if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("MMCDXXV"))