def squirrel_play(temp, is_summer):
  if not is_summer and temp>=60 and temp<=90 or is_summer and temp>=60 and temp<=100:
    return True
  return False