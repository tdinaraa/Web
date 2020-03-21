def make_out_word(out, word):
  tagA = out[:2]
  tagB = out[2:]
  return "%s%s%s" % (tagA,word,tagB)