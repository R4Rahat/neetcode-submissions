class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            j = i + 1
            m = arr[j]
            maxIndex = j
            while j < len(arr):
                if arr[j] > m:
                    m = arr[j]
                    maxIndex = j
                j += 1
            arr[i] = arr[maxIndex]

        return arr

        