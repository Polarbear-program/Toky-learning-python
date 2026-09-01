def squirrel_play(temp, is_summer):
  # Default condition: If 60 <= temp <= 90: Always True
  if (temp >= 60) and (temp <= 90):
    return True
  # Second condition: If is_summer True, then: 60 <= temp <= 100
  elif (temp >= 60) and (temp <= 100) and is_summer is True:
    return True
  # Else: everything will be false
  else:
    return False
  
print(squirrel_play(50, True))
print(squirrel_play(95, True))
print(squirrel_play(75, False))