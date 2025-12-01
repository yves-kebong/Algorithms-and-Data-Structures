def maxsubarray(nums):
  max_nums = float("-inf")
  l=lenf(nums)
  for i in range(l):
    actual_sum=0
    for j in range(i , l):
      actual_sum = actual_sum + num[j]
      max_nums =  max(max_nums , actutal_sum)
  return max_num
