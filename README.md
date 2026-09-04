## THIS IS MY PROGRESS OF LEARNING HOW TO CODE - [PYTHON MOSTLY]

### [WARNING] ###
> This update can be very attractive to the viewer's eyes. If this happens to some of you, I just want to let you know that. Have a great day, and please fix any issues in your life.

<p align="center">
  <img src="Others/Artboard4.png" alt="Toky_first_git_avatar" width="356" height="356" />
</p>

---
### SUMMARY ###
A not-so-organized roadmap of Toky-programming's study since July 24th, 2026. It first started with variables and conditions, and then slowly
progressed to loops, functions, lists, etc. At first, I was not really serious about coding at all, but it takes some courage as well as discipline to get this far.
> It's hard to just write a new README.md from scratch since I didn't really do this before. But this could act as a second journal, mostly for updating what I've learned about programming.
---

### THE LOG ###
#### [August 3rd, 2026 [WHAT I HAVE LEARNT]] ####
- Dictionary
- Binary Search/Linear Search
- Recursion
- Python List
---

#### [August 4th, 2026] ####
- Little bit of DBMS(Database management system)
- LLMs(Large-language models), API(Application Programming Interface)
RLHF(Reinforcement Learning from Human Feedback)
- Calling a function in Python (but not really knowing how a function works)
- Python Classes and Objects(OOP)
- Differences between for loop and while loop
- Install Github -> Create a batch -> Make a push -> make a pull
---

#### [August 5th, 2026] ####
- File Handling in Python
- Quick Sort
- Set, list and its methods in Python Datatype
- Math needed for programming
- Do I need to learn discrete math too?
 [!Maybe later, finish all Python first]
---

#### [August 6th, 2026] ####
- Notion
- You need to "fork" to make a request to change someone else's project on GitHub, or make a clone of their code on the GitHub server
- I still can change others' projects, but they will have to accept the changes
---

#### [August 11st, 2026] ####
- function, accessing function, parameters & arguments, scope within function, kwargs
- Git push, pull, create repository right on GitHub Desktop
- Stack
- numpy, matplotlibpyploy library
- Manipulating arrays and subarrays
---

#### [August 15th, 2026] ####
- Import module, which is a file of code, using import and from
- Understand the usage of lists, tuples(useless), and sets
- Create the first snake game using the turtle library in Python, to create the screen of the application: + Screen() method, title, setup(for width and height of the game), bgcolor, tracer(0) is to turn off the screen update
- Create a moveable project using direction, xcor(), ycor(), setx(), sety()
- Create a key press setting using key.listen() method and onkeypress(direction,key)

#### [August 16th, 2026] ####
- Carry on with programming snake game, by creating segment for the snake
- Turtle() method in turtle library is object, Screen() method is for screen
- The object penup() method should be put before goto() method, to stop before it already appeared there
- Using inheritance in snake game to make the code cleaner and more organized
- It seems like every class call, you have to contain one __init__ method... 
  -> To use the instance of the function without having to interfere with the class 

#### [August 17th, 2026] ####
- Quick learn about bubble sort, selection sort, insertion sort. Understand the fundamentals of algorithms
- OOP: Understand clearer the implementation of inheritance, why the child class will override its parents inheritance when it has its own __init__ method. But this will cause the child class to have its own properties; that's why super().__init__(property you want to access from parents or sibling class) comes to play

- Get used to Turtle() method in <turtle library>. Create a basic graph
---

#### [August 18th, 2026] ####
- Messing with the <json> library, create one, open one using file handling in Python. with open("mod.json", "r") as file. And json.load(file) to convert a JSON string to Python
- Created my personal LICENSE
- Analyzing and learning the fundamentals of a program
- Using git add name.file to add a single file, git add . or git add --all or git add -A - for staging all changes
- Using git commit -m "message" to update the status of changes within the project
- Understand <ATTRIBUTE> that property of a class; an attribute represents the quality of the class or object: Age, hair color, address, max speed, min speed, etc
- Using the turtle library again, with a clearer understanding of screen.tracer(), screen.delay(), turtle.write("message", align="", font=()) method
---

#### [August 20th, 2026] ####
- Understand the use of turtle.left(angle turn left) and turtle. right(angle turn right) method in directing the object. turtle.fd(steps) will program the distance of your first step and the ongoing steps of an object
- screen.textinput()
- Learn the fundamentals of queues, which is first-in-first-out, it can be implemented for e-ticket queue, select first ticket that went first: Enqueue for adding element to the last of list, dequeue to delete/return element from the first index, peek is return the first element from list, isEmpty to check if list is empty, and Size is the amount of element in queue aka len(queue) method
---

#### [August 21st, 2026] ####
- Learn linked list, understand the differences between linked list and array. Know how to build a linked list data structure via coding and know that it's harder and requires more coding lines than an array data structure since a linked list doesn't have built-in support as an array does.
- Linked list:
   - This way, a node can understand that it needs to store a value and link to nothing, which later links to another node
  >     class Node:
  >       def __init__(self, value):
  >          self.value = value
  >          self.next = None
  >
  - This way, a node in a linked list can be traversed to the next node and printed out
  >     def traverse_Print(head):
  >       # Current node will store the value
  >       currentNode = head
  > 
  >       # While the current node exists,
  >       # a loop will occur to make sure the next node exists
  > 
  >       while currentNode:
  >          # Print the current node first, next node carry on later
  >          # print(currentNode.value, end= " -> ")
  >          currentNode = currentNode.next
  > 
  >       # After no node is found in the next turn, print "null"
  >       print("null")
  - Create a function that find lowest value in linked list nodes:
  
  >      def findLowValue(node):
  >         lowValue = node.value
  >         # The currentNode = node.next is just a Node pointer
  >         # pointing to the next node address
  >         # Which is why when comparing lowValue with currentNode
  >         # must have .value to select the value, not the address
  >         currentNode = node.next
  > 
  >         while currentNode:
  >          # If the lowest value is greater than the next value,
  >          # the next value is definitely lower, so the lowest value = next value
  >          if lowValue > currentNode.value:
  >            lowValue = currentNode.value
  >            # After comparison, next node will be linked
  >           currentNode = currentNode.next
  > 
  >     print(lowValue)
  >  
  -   Understand, in every function created specifically for linked-list, the function(node/head) parameter always works as Node intended, not a value like int, str, float
---

#### [August 22nd, 2026] ####
- First time solved a problem without needing to ask AI, internet, or a friend. Getting used to
calling a function, parameter, loop to solve an array-related problem
- Understand the linked-list mechanism and traverse and delete it
---

#### [August 23rd, 2026] ####
- Understand the function insertNewNode clearer. When a new Node created, it will replace currentNode
next pointer to point to the next node, then,
the current node's next pointer will point to the new node:
 >     newNode.next = currentNode.next
 >     currentNode.next = newNode
 >     return currentNode

- Understand the mechanism of the removeNode(head, nodeRemove) function:

 >     if head(currentNode) == nodeRemove:
 >       return currentNode.next (nothing happens, carry on with pointer pointing to next node)
 > 
 >     while currentNode.next is not nodeRemove:
 >       currentNode = currentNode.next

 >     if currentNode.next is None:
 >       return currentNode
 >     currentNode.next = currentNode.next.next  
---

  #### [August 24th, 2026] ####
  - Almost everything in Python is an object with properties and methods(No wonder it so slow)
  - __init__() is an built-in method in Python that help you to initiate the class itself when you call call it.
  - (self) parameter is a reference to the instance of a class. Without self, the class wouldn't know which object's properties you want to access
  - (self) does not need to be named self.
  - Class in class, the implementation. It is really useful to organize my code, because it will inherit the properties and methods of the outer class
  - Encapsulation: Using the double underscore __ prefix will make the variable become private. And to access the private variable, I will need a return function to access it, or use it within the class. 
---

  #### [August 26th, 2026] ####
  - Create a list with 10 empty elements; know that it will use Unicode to track the position of each "bucket" in a hash(no fucking clue, I will learn again later)
  - id(variable) to find the memory address of the variable, hex(id(variable)) to cast into heximal
---

 #### [August 27th, 2026] ####
  - I've spent all day making a logo for a company, so I didn't study much today. Only made one simple_math using the class, def to create a power and square root function
---

 #### [August 28th, 2026] ####
  - Permutate function, hashmap(dictionary) implementation, quickSort easier
  - Binary Tree, how to create one, connect binary tree node. A -> (B, C), B ->..., C->...
        -> Learn the relation between each Node; for instance, the dashed lines connecting each Node are paths.
        -> A is the "parent/root function; B and C are child functions of A. If the child function connects to None(null), then it will be the "leaf nodes"
        - A subtree with B is "the Root"
  - Binary trees have many types based on multiple factors:
    - On the basis of Number of Children: Full Binary Tree, Degenerate Binary Tree, Skewed Binary Trees
    - On the basis of Completion of Levels: Complete Binary Tree, Perfect Binary Tree, Balanced Binary Tree
    - On the basis of Node Values: Binary Search Tree, AVL Tree, Red Black Tree, B Tree, B+ Tree, Segment Tree

  - Reverse Linked list using 3-pointer method, prev - curr - next pointer. The "previous" will first point at None(null), "the current" node will be the node that points to the value; and lastly, "next pointer" points to the node after the current pointer
---

 #### [August 30th, 2026] ####
  - Today I've decided to do some basic logic problems to enhance my fundamentals of solving problems(or maybe because today I'm lazy) in programming, like: Even and odd check, multiplication table, Sum of natural
  - Also learn to use recursion in some problems; C syntax could also be applied in Python: print("%d * %d = %d" % "n, i, n * i")
      => I struggled a lot during the program for the sum of natural numbers, mostly syntax
      => For fuck sake, I should have also been more careful with the variable name; one wrong name and the recursion just repeats itself forever
  - Maybe do some problems with a specific variable type, like "string - str", like: make_out_word, extra_end, make_tags, first_two, first_half, without_end,...
---

#### [August 31st, 2026] ####
- Last day of the month. I've been learning quite a lot actually, from data types variable of Python; to linked lists, traversing the node, binary tree, making a project, and solving problems.
- But I feel like I still have so much to learn, and there're some invisible forces within me that pressure me inside. I'm really afraid the day my day cut off his monthly support, and I'll have to figure out a way to make money, there will be no time and joy left for me to study. So now I'll have to push, and maybe cutting edges...
---

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
✅ Trees
⬜ Hash Tables
✅ Graphs
✅ Time complexity (Big O)
✅ Object-Oriented Programming (in more depth)

## QUESTION
- PIP, Modules, Iterators, RegEx ✅
- Queues, Linked Lists, Trees  ✅
- Function *args, **kwargs
- Learning about matplotlib, turtle, time library in Python

## CREDITS
* [Tokyx-Polarbear - Owner](https://github.com/Polarbear-program)
* [Jonathan Bronstein - Advisor](https://github.com/Bronstein0x113c1c3)
* [Giám Dog - Tutor](https://github.com/HungLeAnh)
* [Noah Trần - Advisor](https://github.com/Coder-Blue)
