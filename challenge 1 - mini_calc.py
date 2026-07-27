def operations(num1, num2):

    print("Addition :", num1 + num2,
          "\nDifference :", num1 - num2,
          "\nMultiplication :", num1 * num2,
          "\nDivision :", f"{num1 / num2:.1f}" if num2 != 0 else "undefined")

if __name__ == "__main__" :

    num1 = int(input())
    num2 = int(input())
    
    operations(num1, num2)
