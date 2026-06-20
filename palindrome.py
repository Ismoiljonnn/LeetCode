class Solution:
  def isPalindrome(self, x):
    if x < 0 or (x % 10 == 0 and x != 0):
      return False
      

    reversed_num = 0
    original = x

    while x > 0:
      reversed_num = (reversed_num * 10) + (x % 10)
      x //= 10

    return original == reversed_num