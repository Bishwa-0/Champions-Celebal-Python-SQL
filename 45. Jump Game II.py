class Solution:
    def jump(self, nums: list[int]) -> int:
        step = 0
        end = 0
        far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                step += 1
                end = far
        return step
