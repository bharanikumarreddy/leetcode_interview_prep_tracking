class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        output=0
        current_output= 0
        v=set('aeiou')
        for r in range(0,k):
            if s[r] in v:
                current_output+=1
            output=current_output
        for r in range(k,len(s)):
            if s[r] in v:
                current_output+=1
            if s[r-k] in v:
                current_output-=1
            output=max(output,current_output)
        return output 




            

        
