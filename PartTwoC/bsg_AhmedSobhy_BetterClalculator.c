#include <stdio.h>
#include <math.h>

double add(double num1, double num2){
    return num1+num2;
}

double sub(double num1, double num2){
    return num1-num2;
}

double mul(double num1, double num2){
    return num1*num2;
}

double div(double num1, double num2){
    return num1/num2;
}

double logg(double base,double num)
{
    num=log2(num);
    base=log2(base);
    return (num/base);
}

double power(double base, double powerr)
{
    return pow(base,powerr);
}

double factorial(double num)
{
    for(int i=num-1;i>0;i--)
        num*=i;
    return num;
}

int main()
{
    double firstNumber,secondNumber,ans;
    char operation;
    printf("Enter the first Number: ");
    scanf("%lf",&firstNumber);
    printf("\nEnter the second Number: ");
    scanf("%lf",&secondNumber);
    printf("\nChoose the operation:\n+ : for addition\n- : for subtraction\n* : for mulplication \n/ : for division\n");
    printf("! : for factorial\n^ : for power\ng : for log\n");
    scanf(" %c",&operation);
    switch (operation)
    {
        case '+':
            ans=add(firstNumber,secondNumber);
            break;
        case '-':
            ans=sub(firstNumber,secondNumber);
            break;
        case '*':
            ans=mul(firstNumber,secondNumber);
            break;
        case '/':
            ans=div(firstNumber,secondNumber);
            break;
        case '!':
            printf("!%lf=%lf !%lf=%lf",firstNumber,factorial(firstNumber),secondNumber,factorial(secondNumber));
            return 0;
            break;
        case '^':
            ans=power(firstNumber,secondNumber);
            break;
        case 'g':
            ans=logg(firstNumber,secondNumber);
            break;
        default:
            printf("invalid operation\n");
            return 0;
            break;
    }
    printf("final answer is %lf",ans);
}