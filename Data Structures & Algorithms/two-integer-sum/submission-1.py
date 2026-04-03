class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            d[val] = i
        
        for i, val in enumerate(nums):
            c = target - val
            ci = d.get(c)
            if ci is not None and ci != i:
                result = [ci, i]
                result.sort()
                return result

            

        