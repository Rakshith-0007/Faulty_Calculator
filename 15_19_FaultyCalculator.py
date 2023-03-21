# Excecise 2 -->FaultyCalculator

print("Select the operator\n","+\n -\n *\n /\n")
num1=input()
num2=(input("Enter the first Number\n"))
num3=(input("Enter the Second Number\n"))
num4=num2+num1+num3

if num4=="45*3" or "3*45":
    print("Your answer is:","555")

elif num4=="56+9" or "9+56":
    print("Your answer is:","77")

elif num4=="56/6":
    print("Your answer is:","4")

elif num1=="+":
        print(int(num2)+int(num3))

elif num1=="-":
        print(int(num2)-int(num3))

elif num1=="*":
        print(int(num2)*int(num3))

elif num1=="/":
        print(int(num2)/int(num3))

else:print("Invalid Entry")

