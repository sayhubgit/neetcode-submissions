class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        dic = dict()
        for num in nums:
            if num > 0:
                dic[num] = True
        

        for i in range(1, n+1):
            if i not in dic:
                return i
        return n+1