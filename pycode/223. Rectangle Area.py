class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
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
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        diffx = (C - A) + (G - E) - (max(C,G) - min(A, E))
        diffy = (D - B) + (H - F) - (max(D, H) - min(B, F))
        area3 = diffx*diffy if diffx > 0 and diffy > 0 else 0
        return area1 + area2 - area3