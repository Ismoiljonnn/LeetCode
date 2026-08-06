class Solution:
  def smallestNumber(self, n: int, t: int) -> int:
    def digit_product(num):
      prod = 1
      while num > 0:
        prod *= num % 10
        num //= 10
      return prod

    curr = n
    while True:
      if digit_product(curr) % t == 0:
        return curr 
      curr += 1