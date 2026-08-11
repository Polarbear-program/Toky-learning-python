# Creating a list of food in McDonald with prices using python dictionary

# Creat Keys -> Values. Ex: Key: Big Mac, values: 5.12
menu_Mac = {
    "Big Mac":  5.12,
    "French Fry": 3.99,
    "Mc Flurry": 2.99,
    "Quarter Pounder": 5.99,
}

# Dictionary can has keys as numbers, strings and vice versa
phone_book = {
    826: "Toky old number",
    722: "Toky new number",
    818: "Dad's number",
    668: "Mom's number",
}

# And dictionary can also store another dictionaries
character_menu = {
    "North_side": {"Toky": 100, "Min": 70, "Lam": 80},
    "South_side": {"Foxxy": 120, "Puppy": 60, "Aoi": 100},
    "West_side": {"Mocha": 150, "Ebrina": 40, "Mecca": 110},

}

"""# Add value, like Shamrock dish
menu_Mac["Shamrock"] = 6.99

# Update price of Big Mac to 5.99
menu_Mac["Big Mac"] = 5.99
print(menu_Mac)

# Find value(price) of Mc Flurry in menu MacDonald
find_value = menu_Mac["Mc Flurry"]
print("The price of Mc Flurry is: $", find_value)

find_phone = phone_book[668]
print("The phone's number is belongs to", find_phone, '\n') """

# This will select the character set based on region
select_char_region = character_menu["North_side"]

# This will select character based on keys
select_char = character_menu["South_side"]["Foxxy"]
print("Display:", select_char_region, '\n')
print("Price of selected character:", select_char, '\n')

# Display only the key in character_menu, which is the region of characters
for dis_key in character_menu.keys():
    print(dis_key)
print('\n')

"""# Display only the value in character_menu dictionary, which is all the character of each regions + price
for dis_char in character_menu.values():
    print(dis_char)"""

# Display all values and keys in character_menu dictionary, this use dictionary_name.item() method:
for dis_all in character_menu.items():
    print(dis_all)

# How to check value of keys, using "value_name" in dictionary_name like:
"Toky" in character_menu

for characters, prices in character_menu["North_side"].items():
    if prices < 100:
        print(characters + " price :" + str(prices) + "$")
