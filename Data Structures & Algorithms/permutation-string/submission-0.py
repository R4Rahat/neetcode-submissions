class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1) - 1

        while j < len(s2):
            string = s2[i:j+1]
            if sorted(s1) != sorted(string):
                i += 1
                j += 1
            else:
                return True

        return False