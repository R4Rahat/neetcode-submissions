class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        output = []
        for s in strs:
            if str(sorted(s)) not in obj:
                obj[str(sorted(s))] = [s]
            else:
                obj[str(sorted(s))].append(s)

        for o in obj.values():
            output.append(o)

        return output