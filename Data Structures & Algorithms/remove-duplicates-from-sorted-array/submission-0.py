class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        i = 0 
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                l += 1
                nums[l] = nums[j]
            i += 1
            j += 1
        return l + 1