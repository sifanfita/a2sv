from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        q = deque([(root, 1)])  # (node, index)

        while q:
            offset = q[0][1] * 2
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                node, index = q.popleft()
                if node.left:
                    q.append((node.left, index * 2 - offset))
                if node.right:
                    q.append((node.right, index * 2 + 1 - offset))

        return ans
