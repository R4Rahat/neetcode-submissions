class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        output = []
        for s in strs:
            ss = str(sorted(s))
            if ss not in obj:
                obj[ss] = [s]
            else:
                obj[ss].append(s)

        for o in obj.values():
            output.append(o)

        return output