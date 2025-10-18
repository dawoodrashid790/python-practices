num1 =float(input("enter your first number:"))
num2 = float (input("enter your second number:"))
operator =input("ENTER THE OPERATOR(+,-,*./):")
if operator =="+":
    result =num1+num2         
elif operator =="-":
    result =num1-num2
elif operator =="*":
    result = num1*num2
else:
     result= "error:invalid operator"
print ("RESULT:",result)
fruits=["avacado", "cherry", "apple", "banana", "mango"]
for x in fruits:
    print (x)
    if x==fruits[0]:
        break