# Question 7
print("Question 7")
print ("Enter a number ")
user_input = int(input())

number_list = [10, 20, 30, 40]


index = 0


def check_number(n):
    global index


    if index < len(number_list) and n == number_list[index]:
        print(f"The number {n} exists in the list")

    else:
        if index < len(number_list):
            index += 1
            check_number(n)


        else:
            print(f"The number {n} does not exist in this list")


check_number(user_input)



#Question 8
import random
print("")
print("Question 8")
number = range(4)

number_list = []

for n in number:
    number_list.append(str(random.randint(0, 1)))


finished_product = "".join(number_list)

# Converting the binary number to decimal

print(f"The binary value is: {(finished_product)}")
print(f"Its decimal equivalent is {int(finished_product,2)}")


# Question 9
print("")
print("Question 9")
first_number = 0
second_number = 1
fibonacci_sum = first_number+second_number

fibonacci_list = [first_number, second_number] # To hold all the fibonacci together so that I can sum them up later
for i in range(48):
    c = first_number + second_number  # This will get the sum of the variable 'first_number' and 'second_number' for each execution

    first_number = second_number
    second_number = c

    fibonacci_sum+=c

    fibonacci_list.append(c)


# Sum of the fibonacci
print(f"The sum of the first 50 fibonacci is {sum(fibonacci_list)}")
print(f"The sum of the first 50 fibonacci (wihtout using the list method) is  {fibonacci_sum}")


