def array123(nums):
    nnums = set()

    for i in nums:
        nnums.add(i)
    subnums = {1, 2, 3}
    if subnums.issubset(nnums):
        return True
    return False