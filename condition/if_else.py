student = True
credit = True
behavior = False

if (credit == behavior) != student:
    print("Student is eligible for scholarship")

elif (credit and behavior) and not student:
    print("Student is not eligible for scholarship")

else:
    print("Student is not eligible for scholarship")

#if statement always default true
if student:
    print("Student is indeed a student")

#this will be old enough to access a website
age = 24
if age >= 18:
    print("Congrats! You are mature enough ")
else:
    print("You must ask your parents for permission first")


