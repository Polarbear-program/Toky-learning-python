def date_fashion(you, date):
    # Default: If either you or date <= 2 then return 0
    if (you <= 2) or (date <= 2):
        return 0
    # If none of you <=2 + either you or date >= 8 then return 2
    elif (you >= 8) or (date >= 8):
        return 2
    # Everything else will return 1
    else:
        return 1


print(date_fashion(5, 2))  # Return 0
print(date_fashion(8, 2))  # Return 0
print(date_fashion(9, 5))  # Return 2
print(date_fashion(5, 7))  # Return 1
