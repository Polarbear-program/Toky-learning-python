# Learn queue on python
# Firt import queue library
import queue as q

# Create an empty list using queue library
list = q.Queue()

# Create an empty list without using library
list_2 = []

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
un_sort_num = [12, 54, 21, 2, 5, 1, 53, 14, 42]

# putting value into the end of the list, also known as enqueue
# Using queue.put(value) method to add each value singly in an order
for value in numbers:
    list.put(value)

# Putting number in unsorted number into list 2 using append() method of list
for number in un_sort_num:
    list_2.append(number)

# Access value at the first index one by one in the list number, this is known as peek
"""print(list.get())
print(list.get())
print(list.get())
"""
for i in range(len(list_2)):
    print(list_2[i], end=" ")

# Enqueue
# Dequeue
# Peek
# isEmpty
# Size