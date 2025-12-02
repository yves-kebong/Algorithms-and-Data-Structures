def maxsubarray(nums):
  max_num = float("-inf")
  l=len(nums)
  for i in range(l):
    actual_sum = 0
    for j in range(i,l):
      actual_sum = actual_sum +nums[j]
      max_sum = max(max_sum ,actual_sum)
  return max_sum
