 #?task1

# first_name=input('please enter your first name: ')
# last_name=input('please enter your last name: ')
# print(f"{last_name[::-1]} {first_name[::-1]}")


#? task2

# num=int(input("please enter number"))
# result=num+num**2+num**3
# print(result)


#? task3

# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)


#? task4

# volume=(4/3)*(3.14)*(6**3)
# print(volume)

#? task5

# base=int(input('please enter base: '))
# height=int(input('please enter height: '))
# area=(0.5)*base*height
# print(area)


#? task6
# r=6

# for row in range(r):
#     for col in range(row):
#         print("*",end=" ")
#     print()

# for row in range(r-1):
#     for col in range(r-row-2):
#         print("*",end=" ")
#     print()

#? task7

# word=input('please enter word: ')

# print(f"{word[::-1]}")


#? task8

# for num in range(7):
#     if num==3 or num==6:
#         continue
#     print(num)


#? task9

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# fib(50)

#? task10

# text = input("Enter a string: ")

# digits_counter = 0
# letters_counter = 0

# for char in text:
#     if char.isdigit():
#         digits_counter += 1
#     elif char.isalpha():
#         letters_counter += 1

# print(digits_counter,letters_counter)

##############################################################################

#? task1

# def remove_adjacent_duplicates(numbers):
#     result = []
#     for number in numbers:
#         if len(result) == 0 or number != result[-1]:
#             result.append(number)
#     return result

# print(remove_adjacent_duplicates([1,1,1,2,3,3,3,4,4]))


#? task2

# a=input("please enter a: ")
# b=input("please enter b: ")
# def split_string(x,y):

#     x_front=x[:(len(x)//2)+len(x)%2]
#     x_back=x[(len(x)//2)+len(x)%2:]

#     y_front=x[:(len(y)//2)+len(y)%2]
#     y_back=x[(len(y)//2)+len(y)%2:]

#     return x_front + y_front + x_back + y_back

# print(split_string(a,b))


#? task3

# def check_list(ls):
#     return len(ls)==len(set(ls))

# print(check_list([1,2,3,4]))


#? task4

# def bubble_sort(unsorted_list):
#     n = len(unsorted_list)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if unsorted_list[j] > unsorted_list[j+1]:
#                 unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
#     return unsorted_list

# print(bubble_sort([1,5,2,3,9,6]))



#? task5


# import random

# def guess_number():

#     number = random.randint(1, 100)

#     tries = 10
#     guessed_numbers = []

#     while tries > 0:
#         guess = input("guess a number between 1 and 100: ")
#         if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
#             print("invalid input. Please enter a number between 1 and 100.")
#             continue

#         guess = int(guess)


#         if guess in guessed_numbers:
#             print("You've already guessed this number. Try a different one.")
#             continue

#         guessed_numbers.append(guess)


#         if guess == number:
#             print("Congratulations! You guessed the number in", 10 - tries + 1, "tries.")


#             play_again = input("Do you want to play again? (y/n) ")
#             if play_again.lower() == "y":
#                 guess_number()
#             else:
#                 print("Thanks for playing!")
#             return


#         elif guess > number:
#             print("The number is lower than", guess)
#         else:
#             print("The number is higher than", guess)

#         tries -= 1


#     print("You didn't guess the number. The number was", number)


#     play_again = input("Do you want to play again? (y/n) ")
#     if play_again.lower() == "y":
#         guess_number()
#     else:
#         print("Thanks for playing!")

# guess_number()

