def calculate (action, firstNum, secondNum) :
   if action == "add":
     result = firstNum + secondNum
     return result

   if action == "subtract":
     result = firstNum - secondNum
     return result

calcReturn = calculate("subtract", 10, 5)
calcReturn = calculate("add", calcReturn, 5)  

print(calcReturn)

