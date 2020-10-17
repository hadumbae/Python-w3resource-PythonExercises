# Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers. Go to the editor

# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

listString = input('Please enter a string of numbers : ')

stringList = listString.split(',')

# Method 1
stringTuple1 = tuple(stringList)

# Method 2
stringTuple2 = (*stringList,)

print(stringList)
print(stringTuple1)
print(stringTuple2)
