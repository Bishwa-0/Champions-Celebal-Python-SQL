class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        bishwa = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[bishwa]:
                bishwa += 1
                nums[bishwa] = nums[i]
        
        return bishwa + 1
