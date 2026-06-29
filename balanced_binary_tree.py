# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isBalanced(self, root):

    def check_height(node):
      if not node:
        return 0
      
      left = check_height(node.left)
      if left == -1:
        return -1
      
      right = check_height(node.right)
      if right == -1:
        return -1
      
      if abs(left - right) > 1:
        return -1

      return max(left, right) + 1

    return check_height(root) != -1