# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)


# re-declaring the variable works

f="abc"
print(f)

# ERROR: variables of different types cannot be combined
# Must define the 123 as string before print or python will throw an error
print("This is a string" + str(123))

# Global vs. local variables in functions

def someTestFunction():
    # this sets f as global. the prior f declaration is no longer used
    global f
    f="def"
    print(f)

someTestFunction()
print(f)

# undefine variable in real time
del f
print(f)