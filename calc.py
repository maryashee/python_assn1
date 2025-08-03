num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
operation =input("Enter the operation (+, -, *, /): ")

if operation=="+" :
    result= num1 + num2
    print(f"{num1} + {num2}= {result}")

elif operation=="-" :
    result= num1-num2
    print(f"{num1} - {num2} = {result}")

elif operation=="*" :
    result= num1*num2
    print(f"{num1} *{num2}= {result}")

elif operation=="/" :
      if num2 !=0 :
        result=num1/num2
        print(f"{num1} /{num2}= {result}")
        
      else :print("error!")

