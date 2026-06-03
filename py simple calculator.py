while True:

    print("Simple calculator")


    num1 = float (input("enter first number: "))
    num2 = float(input("enter second number: "))


    operation = input("choose operation (+,-,*,%,/):")


    if operation =="+":
       print("answer:", num1 + num2 )


    elif operation == "-":
       print("amswer:", num1 - num2 )


    elif operation == "*":
       print("answer:", num1 * num2 )


    elif operation == "%":
       print("answer:",num1 % num2 )


    elif operation == "/":
       print("answer:", num1 / num2 )


    else:
       print("invalid operation")
    again = input("do u want another calculation? (yes/no): ")
    if again == "no":
     print("goodbye")
     break
  
