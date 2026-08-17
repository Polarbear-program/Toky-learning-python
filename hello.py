import json

# Open json file required importing json library
with open("mod.json", "r") as file:
    
    # Create a varible specified for reading json information. 
    # The json.load() method is to convert JSON string to Python
    data = json.load(file)

# Print out information of this project...
print(f"This is: {data["id"]}")
print(f"Made by: {data["author"]}")
print(data["version"])
