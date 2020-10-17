# Write a Python program which accepts the user's first and last
# name and print them in reverse order with a space between them.

firstName = input('First Name : ')
lastName = input('Last Name : ')

# Method 1
print(lastName + ' ' + firstName)

# Method 2
print(f'{lastName} {firstName}')
