# Write a Python program to accept a filename from the
# user and print the extension of that. Go to the editor

# Sample filename : abc.java
# Output : java

filename = input('Please enter filename : ')

print('File Extension Is : ' + filename.split('.')[-1])
