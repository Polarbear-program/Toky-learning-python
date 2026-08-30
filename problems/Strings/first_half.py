# Given a string of even length, return the first half. 
# So the string "WooHoo" yields "Woo".
#________________________________________#
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc

def first_half(str):
  first_half = len(str)/2
  return str[:first_half]
