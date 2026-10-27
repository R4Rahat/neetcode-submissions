class Solution:
    def encode(self, strs: List[str]) -> str:
        # encoded = ""
        # for i in strs:
        #     l = len(i)
        #     encoded += str(l) + "#" + i
        # return encoded
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append("#")
            res.append(i)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


        