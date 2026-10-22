class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # for i in range(len(nums)):
        #     if nums[i] not in freq:
        #         freq[nums[i]] = 1
        #     else:
        #         freq[nums[i]] += 1

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        arr = []
        for num, ind in freq.items():
            arr.append([ind, num])
        
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
        