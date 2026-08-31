"""def cigar_party(cigars, is_weekend):
  if cigars <= 60 and cigars >= 40  and is_weekend == False:
    return True
  elif cigars >= 40 and is_weekend == True:
    return True
  else:
    return False"""

# Easier way
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)


print(cigar_party(40, True))
