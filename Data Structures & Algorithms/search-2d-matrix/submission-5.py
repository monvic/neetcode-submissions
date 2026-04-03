class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) -1

        while top <= bot:
            mid = (top+bot)//2
            print(top, mid, bot)
            if target < matrix[mid][0]:
                bot = mid -1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        if bot < top:
            print("False")
            return False
        
        print("Binary Search")
        r = matrix[mid]
        start = 0
        end = len(matrix[mid]) -1 
        while start <= end:
            m = (start+end)//2
            if r[m] == target:
                return True
            elif target < r[m]:
                end = m - 1
            elif target > r[m]:
                start = m + 1
        
        return False
        
        
