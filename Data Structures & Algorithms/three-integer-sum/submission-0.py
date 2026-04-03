class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        result = []
        for start in range(0, len(nums)-2):
            for mid in range(start+1,len(nums)-1):
                for end in range(mid+1,len(nums)):
                    # print(nums[start], nums[mid], nums[end])
                    s = nums[start] + nums[mid] + nums[end]
                    if s == 0:
                        rs = [nums[start], nums[mid], nums[end]]
                        rs.sort()
                        # print(rs)
                        if rs not in result:
                            # print(rs)
                            result.append(rs)
        return result
        

            

        