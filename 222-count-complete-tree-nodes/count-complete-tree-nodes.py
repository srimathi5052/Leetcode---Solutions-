# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
       
        if not root:
            return 0

        left_height = self.getLeftHeight(root)
        right_height = self.getRightHeight(root)

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height