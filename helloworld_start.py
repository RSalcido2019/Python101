#
# Example file for HelloWorld
#
# Built-in print function
print("Hello World")
# Setting the variable to be the input function. Setting the input function to output the command below.
name = input("What is your name? ")
# Print the message with the variable.
print("Nice to meet you,", name)

# defing a function !!!PYTHON USES WHITE SPACES TO FIGURE OUT WHICH LINES OF CODE BELONG TO CODE BLOCKS OR IF STATEMENTS.
# INDENTION IS IMPORTANT !!
# four space indention indicates the code block belongs in the function main()
def main():
    print("Hello World")
    name = input("What is your name? ")
    print("Nice to meet you,", name)


# Code that execute the program

if __name__ == "__main__":
    main()