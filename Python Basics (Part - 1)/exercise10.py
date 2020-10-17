# Write a Python program that accepts an integer (n)
# and computes the value of n+nn+nnn.

# Sample value of n is 5
# Expected Result : 615

number = int(input('Please enter the value of n : '))

n = int(number)
nn = int('%i%i' % (number, number))
nnn = int('%i%i%i' % (number, number, number))

print(n + nn + nnn)
