import collections
class Solution(object):
    def groupAnagrams(self, strs):
        wordMap = collections.defaultdict(list)
        for word in strs:
            wordMap["".join(sorted(word))].append(word)
        solution = wordMap.values()
        for i in solution:
            i.sort()
        return solution
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        