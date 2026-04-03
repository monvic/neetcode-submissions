class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        print(nums)
        for i,val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - val
            r = self.twoSum(nums[i+1: len(nums)], target, val)
            # print(r)
            result = result + r
        # print
        return result


    def twoSum(self, nums, target, val):
        result = []
        # print(nums, target)
        start = 0
        end = len(nums) - 1
        while(start < end):
            sc = nums[start]
            ec = nums[end]

            s = sc + ec
            # print(start, end, sc)

            if s == target:
                result.append([val, sc,ec])
                start += 1
                end -= 1
                while(nums[start] == nums[start-1] and start < end):
                    start+=1
            elif s < target:
                start += 1
                while(nums[start] == nums[start-1] and start < end):
                    start+=1
            else:
                # print()
                end -= 1
                x = nums[end]
                y = nums[end+1]
                print('a', end, x, y)
                while (nums[end] == nums[end+1] and end > start):
                    end -= 1
                    print('b', end, x, y)
        return result
