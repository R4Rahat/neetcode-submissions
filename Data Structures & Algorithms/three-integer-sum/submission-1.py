class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [nums[i],nums[l], nums[r]] not in res:
                        res.append([nums[i],nums[l], nums[r]])
                        l += 1
                        r -= 1
                    else:
                        l += 1
                        r -= 1 
                    

        
        return res
