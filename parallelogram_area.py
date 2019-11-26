#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: November 2019
# This program finds the area of a parallelogram
# with user input


def parallelogram(h, b):
    # this function calculates area of a parallelogram

    # process
    area = b * h
    return area


def main():
    # this function takes input and calls another function

    # input
    print("Let's find the area of a parallelogram!")
    base_from_user = input("Enter the base of the rectangle: ")
    height_from_user = input("Enter the height of the rectangle: ")

    # process
    try:
        base = int(base_from_user)
        height = int(height_from_user)

        # call function
        final_area = parallelogram(b=base, h=height)

        # output
        print("")
        print("Area of the parallelogram is {0}cm^2".format(final_area))
    except Exception:
        print("")
        print("Theses are not integers")


if __name__ == "__main__":
    main()
