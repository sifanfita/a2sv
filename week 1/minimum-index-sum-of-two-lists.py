class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)  # Find common strings
        if not common:
            return []
        min_index_sum = float('inf')
        result = []
        for common_str in common:
            index_sum = list1.index(common_str) + list2.index(common_str)
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                result = [common_str]
            elif index_sum == min_index_sum:
                 result.append(common_str)
        return result
            
           

    
            
        
        
    
        

    

    


        
    
        