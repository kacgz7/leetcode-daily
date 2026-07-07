class Solution(object):
    def containsDuplicate(self, nums):
        og = set(nums)
        if len(og) == len(nums):
            return False
        else:
            return True