# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
      output = []

      def helper(node):
          if not node:
            return

          helper(node.left)
          output.append(node.val)

          helper(node.right)

      helper(root)
      return output
