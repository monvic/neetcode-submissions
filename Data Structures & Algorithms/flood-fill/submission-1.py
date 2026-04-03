class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        i_color = image[sr][sc]
        if i_color == color:
            return image

        def fill(image, sr, sc, color, i_color):
            ROWS, COLS = len(image), len(image[0])
            if min(sc,sr) < 0 or sr>=ROWS or sc>=COLS or image[sr][sc] != i_color :
                return


            image[sr][sc] = color
            
            fill(image, sr+1, sc, color, i_color)
            fill(image, sr-1, sc, color, i_color)
            fill(image, sr, sc+1, color, i_color)
            fill(image, sr, sc-1, color, i_color)
        
        fill(image, sr,sc,color, i_color)
        return image