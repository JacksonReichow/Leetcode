class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {} 
        countT = {}
        #make two hash tables for tracking chars and num of times
        #they appear

        if len(s) != len(t):
            return False
        #make sure strings are same length
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            #counts each letter and times it appears
            #uses get() in case letter hasnt appeared yet in string
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            #if the string chars dont match per char, return false
        return True
