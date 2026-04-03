class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cma = []
        rcma = []
        cm = 1
        for n in nums:
            cm *= n
            cma.append(cm)
        
        rcm = 1
        for i in range(len(nums)-1, -1 , -1):
            rcm *= nums[i]
            rcma.append(rcm)
        rcma.reverse()

        result = []
        for i in range(0, len(nums)):
            cmai = i - 1
            rcmai = i + 1
            mul1, mul2 = 1, 1
            if not (cmai < 0):
                mul1 = cma[cmai]
            if not (rcmai >= len(nums)):
                mul2 = rcma[rcmai]
            result.append(mul1*mul2)
            
        return result
                


        

        
            





# [1,2,4,6]

# [1,2,8,48]
# [48,48,24,6]

# [6, 24, 48, 48]

# [48,24,12,8]
        