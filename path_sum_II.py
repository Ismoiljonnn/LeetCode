# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def pathSum(self, root, targetSum):
    result = []

    def dfs(node, current_sum, current_path):
      if not node:
        return
      
      current_path.append(node.val)
      current_sum += node.val

      if not node.left and not node.right:
        if current_sum == targetSum:
          result.append(list(current_path))
      else:
        dfs(node.left, current_sum, current_path)
        dfs(node.right, current_sum, current_path)

      current_path.pop()
    
    dfs(root, 0, [])
    return result