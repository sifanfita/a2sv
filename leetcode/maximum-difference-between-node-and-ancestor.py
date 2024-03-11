class Solution:
    def maxAncestorDiff(self, root):
        return self.maxAncestorDiffHelper(root, root.val, root.val)
    
    def maxAncestorDiffHelper(self, root, mini, maxi):
        if root is None:
            return 0
        mini = min(mini, root.val)
        maxi = max(maxi, root.val)
        l = self.maxAncestorDiffHelper(root.left, mini, maxi)
        r = self.maxAncestorDiffHelper(root.right, mini, maxi)
        return max(maxi - mini, l, r)