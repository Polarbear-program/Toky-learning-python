# Creating a salary list, counting it using for loop and range()

salary_lst = [11, 15, 20, 23, 43, 50, 80, 100]
amazing_lst = [3, 4, 5] #it's more of an index inside while counting, so index 3, 4, 5 which is 23, 43, 50 will + 10 in the salary list
print("The type of amazing_lst: ", type(amazing_lst))
print("Salary list:", salary_lst)

end_i = len(salary_lst)
for i in range(0, end_i):
    if i in amazing_lst:
        salary_lst[i] += 10
    else:
            salary_lst[i] += 5

print("Salary list after increase by 5:", salary_lst, end= " ")