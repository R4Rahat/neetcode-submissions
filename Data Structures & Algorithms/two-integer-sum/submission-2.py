class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in obj:
                return [obj[needed], i]
            else:
                obj[nums[i]] = i


