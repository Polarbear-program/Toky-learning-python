"""my_lst = [12, 9.5, "Dog", "Jack"]
print(my_lst)

my_lst[1] = 10.3
my_lst[2] = "Cat"
print(my_lst)

my_lst[3] = "Hugo"
my_lst[0] = 14
print(my_lst)

place = "Tokyo"
my_lst.append(place)
my_lst.pop(1)
print(my_lst)
print("The length of my_list is: ", len(my_lst))"""

long_list = ["Pasta", "Spaghetti", "Raviolli", "Pho", "Bun bo hue", "Com tam", "Com suon",
             "Iphone", "Oppo", "Xiaomi", "Huawei", "Japan", "Suzuki", "Vietnam", "Vinfast", "Cafe", "Italy"]
# for key_word in long_list:
#    print("This is " + key_word)

num_list = [4, 6, 2, 1, 0, 8, 99, 12, 15, 21, 17, 62] #How to find the biggest value on the numlist?

max_value = 0
for number_search in num_list:
    if number_search > max_value:
        max_value = number_search

print("So, the biggest value is:", max_value)
print("That's it")
