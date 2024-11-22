try:
    num1=int(input("Enter a Number "))
    num2=int(input("Enter a Number "))
    result= num1/num2
    print("The final result is: ",result)
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("Please enter a correct value")
except:
    print("There is some error")
finally:
    print("i will excecute no matter what")