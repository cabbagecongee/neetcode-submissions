class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            s_key = "".join(sorted(s))
            if d.get(s_key) is None:
                d[s_key] = [s]
            else:
                d[s_key].append(s)
            
        return list(d.values())