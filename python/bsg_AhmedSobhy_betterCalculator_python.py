
equation = input("enter the equation: ")
num1,num2 = 0,0
operation = 'n'

for c in equation:
    if operation=='n':
        if c>='0' and c<='9':
            num1=num1*10
            num1=num1+int(c)
        else:
            operation=c
    else:
        if c>='0' and c<='9':
            num2=num2*10
            num2=num2+int(c)
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def add(x,y):
    return x+y
def min(x,y):
    return x-y
ans=0
try:
    if(operation=='+'):
        ans=add(num1,num2)
    elif operation=='-':
        ans=min(num1,num2)
    elif operation=='*':
        ans=mul(num1,num2)
    elif operation=='/':
        ans=div(num1,num2)
    else:
        operation='n'
except:
    operation='n'
if(operation=='n'):
    print("not valid")
else:
    print(f"your answer is {ans}")