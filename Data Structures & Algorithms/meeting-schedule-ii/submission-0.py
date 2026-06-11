"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        d= defaultdict(int)


        for interval in intervals:
            d[interval.start] += 1
            d[interval.end] -= 1
        
        count = 0
        result = 0
        for key in sorted(d):
            print(key, count, d[key], count+d[key])
            result = max((count+d[key]), result)
            print(result)
            count = count+d[key]

        return result