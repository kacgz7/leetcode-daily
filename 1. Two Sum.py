class Solution(object):
    def twoSum(self, nums, target):
        a = 1
        for i in range(len(nums)):
            if nums[i] + nums[a] == target:
                return [i,a]
            else:
                a += 1
        