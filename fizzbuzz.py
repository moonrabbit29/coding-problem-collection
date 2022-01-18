# so the task is very simple, you will be given two integer i and n : i<n
# print from i -> n but instead of the number you are tasked to print fizz or buzz
# if the number is divisible by 3 print fizz print buzz if its divisible by 5
# if it's divisible by 3 and 5 then print fizzbuzz
# if it's not divisible by either of it print the number

import sys


def fizzbuzz(start, end):
    for i in range(start, end):
        print("{}".format(("fizz" if i %
              3 == 0 else "" + "buzz" if i % 5 == 0 else "") or i))


if __name__ == "__main__":
    start, end = (map(lambda a: int(a), sys.argv[1].split(',')))
    fizzbuzz(start, end)
