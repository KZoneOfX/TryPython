import math
print(math.e)
a = 10
b = 12
print(a+b)
# number = int(input("Enter an integer:"))
# if number < 100:
#     print("Your number is smaller than 100")
# else:
#     print("Your number is greater than 100")

N = 10
sum = 0
count = 0
while count < N:
    number = float(input())
    sum = sum+number
    count = count+1
average = sum/N
print("N = {},Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))
