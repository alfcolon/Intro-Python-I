"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"
print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x:\t%d\ny:\t%f\nz:\t%s" %(x, y, z))

# Use the 'format' string method to print the same thing
print("x:\t{}\ny:\t{}\nz:\t{}" .format(x, y, z))

# Finally, print the same thing using an f-string
string = str(x) + '\n' + str(y) + '\n' + z
print(string.rjust(10, ' '))
