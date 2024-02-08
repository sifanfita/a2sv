class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum=[0]*n

        for start,end,direction in shifts:
            if direction:
                prefix_sum[start]+=1
                if end+1<n: 
                    prefix_sum[end+1]-=1
            else:
                prefix_sum[start]-=1
                if end+1<n: 
                    prefix_sum[end+1]+=1
        
        result=[]
        for i in range(n):
            if i-1>=0:
                 prefix_sum[i]+=prefix_sum[i-1]
            result.append(chr(((ord(s[i])+prefix_sum[i])-97)%26 + 97))

        return "".join(result)
        