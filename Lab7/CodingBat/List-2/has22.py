def has22(nums):
  for i,j in enumerate(nums[:-1]):
    if j == 2 and nums[i+1] == 2:
      return True
  return False