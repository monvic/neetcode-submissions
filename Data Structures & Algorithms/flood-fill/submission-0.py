class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        i_color = image[sr][sc]
        visited = set()
        def fill(image, sr, sc, color, i_color, visited):
        # if i_color == color:
        #     return image
            
            ROWS, COLS = len(image), len(image[0])
            if min(sc,sr) < 0 or sr>=ROWS or sc>=COLS or (sr,sc) in visited:
                return
            visited.add((sr,sc))
            if image[sr][sc] != i_color:
                return
            print(sr, sc, i_color, color)
            image[sr][sc] = color
            
            fill(image, sr+1, sc, color, i_color,visited)
            fill(image, sr-1, sc, color, i_color,visited)
            fill(image, sr, sc+1, color, i_color,visited)
            fill(image, sr, sc-1, color, i_color,visited)
        
        fill(image, sr,sc,color, i_color, visited)
        return image