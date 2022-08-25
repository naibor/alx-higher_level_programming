#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_of_arguments = len(argv)
    count = 1
    if number_of_arguments == 1:
        print("{} arguments.".format(number_of_arguments - 1))
    elif number_of_arguments > 1:
        print("{} arguments:".format(number_of_arguments - 1))
        while count < number_of_arguments:
            print("{}:{}".format(count, argv[count]))
            count = count + 1
