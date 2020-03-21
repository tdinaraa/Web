def centered_average(nums):
  nums.sort()
  avg = sum(nums[1:-1]) / (len(nums) - 2)
  return avg