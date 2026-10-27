class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []
        pre = 1
        suf = 1

        for num in nums:
            prefix.append(pre)
            pre *= num

        for i in range(len(nums)-1, -1, -1):
            suffix.append(suf)
            suf *= nums[i]

        suffix.reverse()

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res


