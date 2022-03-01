#
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 1000

    # conditional flow uses if, elif, else
    if (x < y):
     st = "x is less than y"
    elif (x == y):
     st = "x and y are the same"
    else:
     st = "x is greater than y"
    print(st)
    # conditional statements let you use "a if C else b"


if __name__ == "__main__":
    main()
