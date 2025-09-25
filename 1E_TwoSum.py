class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if nums[i] in diff_map.keys():
                return [i, diff_map.get(nums[i]) ]
            diff_map[temp]=i