class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        floating = 1
        for i in range(len(nums)):
            output[i] = floating
            floating *=nums[i]

        floating = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i]*floating
            floating*=nums[i]
        return output