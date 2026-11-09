class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ret = [intervals[0]]

        idx = 0

        for interval in intervals[1:]:
            curr = ret[idx]
            if curr[0] <= interval[0] <= curr[1]:
                if interval[1] >= curr[1]:
                    ret[idx] = [ret[idx][0], interval[1]]
            else:
                ret.append(interval)
                idx += 1
            
        return ret