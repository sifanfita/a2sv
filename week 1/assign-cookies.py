class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort the greed factors in non-decreasing order
        s.sort()  # Sort the cookie sizes in non-decreasing order

        content_children = 0
        ptr_g = 0  # Pointer for greed factors
        ptr_c = 0  # Pointer for cookie sizes

        while ptr_g < len(g) and  ptr_c < len(s):
            if g[ptr_g] <= s[ ptr_c]:
                content_children += 1
                ptr_g += 1
                
            ptr_c += 1

        return content_children
        