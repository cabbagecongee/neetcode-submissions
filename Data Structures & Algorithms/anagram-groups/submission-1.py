class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sort = "".join(sorted(s))
            if d.get(sort) == None:
                d[sort] = [s]
            else:
                d[sort].append(s)
        
        output = []
        for k in d.keys():
            output.append(d[k])
        return output
