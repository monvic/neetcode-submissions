class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for n in nums:
            if a.get(n) is None:
                a[n] = 1
            else:
                return True
        return False


        