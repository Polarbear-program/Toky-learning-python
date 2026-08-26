## THIS IS MY PROGRESS OF LEARNING HOW TO CODE

> **[!WARNING]**
> This update can be very attractive to the viewer's eyes. If this happens to some of you, I just want to let you know that. Have a great day, and please fix any issues in your life.
>

## SUMMARY
A not-so-organized roadmap of Toky-programming's study since July 24th, 2026. It first started with variables and conditions, and then slowly
progressed to loops, functions, lists, etc. At first, I was not really serious about coding at all, but it takes some courage as well as discipline to get this far.
> It's hard to just write a new README.md from scratch since I didn't really do this before. But this could act as a second journal, mostly for updating what I've learned about programming.

## THE LOG
>> 3rd August, 2026 [WHAT I HAVE LEARNT]
- Dictionary
- Binary Search/Linear Search
- Recursion
- Python List

>> 4th August, 2026

- Little bit of DBMS(Database management system)
- LLMs(Large-language models), API(Application Programming Interface)
RLHF(Reinforcement Learning from Human Feedback)
- Calling a function in Python (but not really knowing how a function works)
- Python Classes and Objects(OOP)
- Differences between for loop and while loop
- Install Github -> Create a batch -> Make a push -> make a pull

>> 5th August, 2026

- File Handling in Python
- Quick Sort
- Set, list and its methods in Python Datatype
- Math needed for programming
- Do I need to learn discrete math too?
 [!Maybe later, finish all Python first]

>> 6th August, 2026
- Notion
- You need "fork" to change someone else's project on GitHub
- I still can change others' projects, but they will have to accept the changes

>> 11th August, 2026
- function, accessing function, parameters & arguments, scope within function, kwargs
- Git push, pull, create repository right on GitHub Desktop
- Stack
- numpy, matplotlibpyploy library
- Manipulating arrays and subarrays

>> 15th August, 2026
- Import module, which is a file of code, using import and from
- Understand the usage of lists, tuples(useless), and sets
- Create the first snake game using the turtle library in Python, to create the screen of the application: + Screen() method, title, setup(for width and height of the game), bgcolor, tracer(0) is to turn off the screen update
- Create a moveable project using direction, xcor(), ycor(), setx(), sety()
- Create a key press setting using key.listen() method and onkeypress(direction,key)

>> 16th August, 2026
- Carry on with programming snake game, by creating segment for the snake
- Turtle() method in turtle library is object, Screen() method is for screen
- The object penup() method should be put before goto() method, to stop before it already appeared there
- Using inheritance in snake game to make the code cleaner and more organized
- It seems like every class call, you have to contain one __init__ method... 
  -> To use the instance of the function without having to interfere with the class 

>> 17th August, 2026
- Quick learn about bubble sort, selection sort, insertion sort. Understand the fundamentals of algorithms
- OOP: Understand clearer the implementation of inheritance, why the child class will override its parents inheritance when it has its own __init__ method. But this will cause the child class to have its own properties; that's why super().__init__(property you want to access from parents or sibling class) comes to play

- Get used to Turtle() method in <turtle library>. Create a basic graph

>> 18th August, 2026
- Messing with the <json> library, create one, open one using file handling in Python. with open("mod.json", "r") as file. And json.load(file) to convert string of JSON to Python
- Created my personal LICENSE
- Analyzing and learning the fundamentals of a program
- Using git add name.file to add a single file, git add . or git add --all or git add -A - for Staging all changes
- Using git commit -m "message" to update the status of change within the project
- Understand <ATTRIBUTE> that property of a class, attribute is represent the quality of the class or object: Age, hair color, address, max speed, min speed, etc
- Using turtle library again, with the clearer understand of screen.tracer(), screen.delay(), turtle.write("message", align="", font=()) method

>> August 20th, 2026
- Understand the use of turtle.left(angle turn left) and turtle right(angle turn right) method in directing the object. turtle.fd(steps) will program how the distance of your first step and ongoing step of an object
- screen.textinput()
- Learn the fundamentals of queues, which is first-in-first-out, it can be implemented for e-ticket queue, select first ticket that went first: Enqueue for adding element to the last of list, dequeue to delete/return element from the first index, peek is return the first element from list, isEmpty to check if list is empty,and Size is the amount of element in queue aka len(queue) method

>> August 21st, 2026
- Learn linked list, understand the differences between linked list and array. Known how to build a liked list data structure via coding and known that it's harder and require more coding lines than array data structure since linked list doesn't have built-in support like array does.
- Linked list:
  > This way a node can understand that it needs to store value and link to nothing, which later link to other node
  - class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

    > This way a node in linked-list can be traverse to the next node, and be printed out
  - def traverse_Print(head):
      > Current node will store the value
      currentNode = head
      > While current node existed, a loop will occur to make sure next node exist 
      while currentNode:
        > Print the current node first, next node carry on later
        print(currentNode.value, end= " -> ")
        currentNode = currentNode.next 
      > After no node found in the next turn, print "null"
      print("null")

  - def findLowValue(node):
      lowValue = node.value
      > The currentNode = node.next is just a Node pointer point to next node address
      > Which is why when comparing lowValue with currentNode must has .value to select the value not the address
      currentNode = node.next

      while currentNode:
        > If lowest value greater than next value, next value definetly lower so that lowest value = next value
        if lowValue > currentNode.value:
            lowValue = currentNode.value
        > After comparison, next node will be linked
        currentNode = currentNode.next
    print(lowValue)
    
    - Understand, in every function created specifically for linked-list, the function(node/head) parameter always work as Node intended, not a value like int, str, flo

>> August 22nd, 2026
- First time solved a problem without needing to ask AI, internet or a friend. Getting used with
calling a function, parameter, loop to solve a array-related problems
- Understand the linked-list mechanism and traverse and delete it

>> August 23rd, 2026
- Understand clearer the function insertNewNode,
when a new Node created, it will replace currentNode
next pointer to point into the next pointer, then,
the current's next pointer will point into new pointer:
  newNode.next = currentNode.next
  currentNode.next = newNode
  return currentNode

- Understand the mechanism of the removeNode(head, nodeRemove) function:
  if head(currentNode) == nodeRemove:
    return currentNode.next (nothing happen, carry on with pointer pointing to next node)
  
  while currentNode.next is not noteRemove:
    currentNode = currentNode.next

  if currentNode.next is None:
    return currentNode
  currentNode.next = currentNode.next.next  

  >> August 24th, 2026
  - Almost everything in Python is object with properties and methods(No wonder it so slow)
  - __init__() is an built-in method in Python that help you to initiate the class itself when you call call it.
  - (self) parameter is a reference to the instance of a class. Without self, the class wouldn't know which object's properties you want to access
  - (self) does not need to named self.
  - Class in class, the implementation. It is really useful to organize my code, because it will inheritant the properties and methods of the outer class
  - Encapsulation: Using double underscore __ prefix will make the variable becomes private. And to access into the private variable, I will need a return function to access it, or use it within the class. 

  >> August 26th, 2026
  Create a list with 10 empty elements

✅ Variables
✅ Conditions
✅ Loops
✅ Functions
✅ Lists
✅ Dictionaries
✅ Searching
✅ Recursion
✅ Sorting
✅ Stacks
✅ Queues
✅ Linked Lists
⬜ Trees
⬜ Hash Tables
✅ Graphs
✅ Time complexity (Big O)
✅ Object-Oriented Programming (in more depth)

## QUESTION
- PIP, Modules, Iterators, RegEx ✅
- Queues, Linked Lists, Trees
- Function *args, **kwargs
- Learning about matplotlib, turtle, time library in Python

## CREDITS
* Tokyx「Polabear」- Author
* Jonathan Bronstein - Advisor
* HungLeAnh - Tutor