class Solution(object):
    def createDict(self, word):
        myDic = {}
        for i in word:
            if i not in myDic:
                myDic[i] = 1
            else:
                myDic[i] += 1
        return myDic
    def isAnagram(self, s, t):
        if self.createDict(s) == self.createDict(t):
            return True
        return False
        
    
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        