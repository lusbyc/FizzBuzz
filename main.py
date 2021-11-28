'''
Fizz-Buzz Challenge

For this challenge you will write a computer program that will display all the numbers between 1 and 100.
For each number divisible by three the computer will display the word “fizz”,
For each number divisible by five the computer will display the word “buzz”,
For each number divisible by both three and five the computer will display the word “fizz-buzz”,
'''

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0: # this line can be refactored as 'if i % 15 == 0:'
        print("fizz-buzz")
        i = i + 1
    elif i % 3 == 0:
        print("fizz")
        i = i + 1
    elif i % 5 == 0:
        print("buzz")
        i = i + 1
    else:
        print(i)
        i = i + 1
