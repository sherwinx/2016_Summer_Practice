
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        areaA = abs(D - B) * abs(C - A)
        areaB = abs(H - F) * abs(G - E)
        intersection = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        return areaA + areaB - intersection
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        