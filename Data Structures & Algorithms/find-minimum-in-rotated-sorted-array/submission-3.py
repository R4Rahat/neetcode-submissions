class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        minimum = nums[0]

        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid - 1
            
            minimum = min(minimum, nums[mid])

        return minimum