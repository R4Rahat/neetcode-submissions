class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isalnum():
                ss += c.lower()
        
        # i = len(ss) - 1
        # mid = len(ss)//2
        # for j in range(0, mid):
        #     if ss[j] != ss[i]:
        #         return False
        #     else:
        #         i -= 1

        # return True

        i = 0
        j = len(ss) - 1
        while i < j:
            if ss[i] != ss[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
