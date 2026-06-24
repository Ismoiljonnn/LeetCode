class Solution:
  def mySqrt(self, x):
    if x < 2:
      return x
    
    left, right = 1, x // 2
    ans = 0

    while left <= right:
      mid = left + (right - left) // 2
      num = mid * mid

      if num == x:
        return mid
      elif num < x:
        ans = mid
        left = mid + 1
      else:
        right = mid - 1

    return ans