def make_chocolate(small, big, goal):
  if (goal>(small+big*5)) or ((goal%5)>small):
    return -1
  elif big*5>goal:
    return goal%5
  else:
    return goal-big*5