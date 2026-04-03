class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s  = set()
        for n in nums:
            s.add(n)
        visited = [0] * len(nums)
        result = 1
        # start, end = 0
        for n in nums:
            start, end = n, n
            s.discard(start)
            while start - 1 in s:
                start -= 1
                s.discard(start)
            while end + 1 in s:
                end += 1
                s.discard(end)
            result = max(result, end - start + 1)
        return result
                



        
    







        