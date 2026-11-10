"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start_sort = sorted(intervals, key=lambda x: x.start) # sort by start time

        for idx, start in enumerate(start_sort[:-1]):
            if start.start == start_sort[idx+1].start or start.start < start_sort[idx+1].start < start.end:
                return False
            
        return True