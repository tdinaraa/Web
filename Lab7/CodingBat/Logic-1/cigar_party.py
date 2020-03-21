def cigar_party(cigars, is_weekend):
  if not is_weekend and cigars >=40 and cigars <=60 or is_weekend and cigars>=40:
    return True
  return False