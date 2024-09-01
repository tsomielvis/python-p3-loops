#!/usr/bin/env python3

def happy_new_year():
    loop_counter = 10
    while loop_counter > 0:
        print(loop_counter)
        loop_counter -= 1
        print("Happy New Year!")
        if loop_counter == 0:
            print("Happy New Year!")
    pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass