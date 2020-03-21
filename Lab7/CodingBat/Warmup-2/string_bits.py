def string_bits(str):
  temp = ""

  for i in range(len(str)):
    if i % 2 == 0:
      temp = temp + str[i]
  return temp