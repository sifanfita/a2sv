class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in range (n):
            image[row] = image[row][::-1]
            for col in range(n):
                if image[row][col] == 1:
                    image[row][col] = 0
                else:
                    image[row][col] = 1
                
                 
        return image