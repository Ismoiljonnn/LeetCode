def two_sum_optimal(nums, target):
  seen = {}

  for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
      return [seen[complement], i]
    
    seen[num] = i

print(two_sum_optimal([2, 7, 11, 15], 9))