class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_1 = [0] * 26
        freq_2 = [0] * 26

        for i in range(len(s1)):
            freq_1[ord(s1[i])-ord('a')] += 1
            freq_2[ord(s2[i])-ord('a')] += 1

        if freq_1 == freq_2:
            return True

        for i in range(len(s1), len(s2)):

            freq_2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            freq_2[ord(s2[i]) - ord('a')] += 1

            if freq_1 == freq_2:
                return True

        return False