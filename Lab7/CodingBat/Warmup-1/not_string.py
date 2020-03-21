def not_string(st):
  if len(st) >= 3 and st[:3] == "not":
    return st
  return "not " + st