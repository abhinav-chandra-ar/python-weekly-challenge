end = int(input("Enter a number : "))
sum = 0
if num > 0:
    for num in range(end+1):
        if num % 2 == 0:
            sum += num

    print("Sum of even numbers  : ", sum)
else :
    print("Enter a natural number!!")
