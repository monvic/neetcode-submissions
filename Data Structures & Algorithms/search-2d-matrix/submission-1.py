class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i, r in enumerate(matrix):
            if r[0] <= target and r[len(r) - 1] >= target:
                print(r)
                return self.binarySearch(r, target)
        return False

    def binarySearch(self, l, target):
        start = 0
        end = len(l) -1 

        while start <= end:
            mid = start + ((end - start)//2)
            print(start, mid, end)
            if l[mid] == target:
                return True
            elif target > l[mid]:
                start = mid + 1
            elif target < l[mid]:
                end = mid - 1
                
        return False


        