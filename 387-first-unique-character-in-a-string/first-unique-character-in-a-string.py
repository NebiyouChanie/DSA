class Solution(object):
    def firstUniqChar(self, s):
        count={}
     
        for i in s:
            count[i]= 1 + count.get( i,0) 
        for index in range(len(s)):
            if count[s[index]]==1:
                return index
        return -1

        