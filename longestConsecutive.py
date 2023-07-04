class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                count += 1
        return count

solution = Solution()
print(solution.longestConsecutive([0,0]))
print(solution.longestConsecutive([100]))
print(solution.longestConsecutive([0,-1]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))


