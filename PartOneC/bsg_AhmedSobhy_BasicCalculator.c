#include <stdio.h>

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

int main()
{
    double firstNumber,secondNumber,ans;
    char operation;
    printf("Enter the first Number: ");
    scanf("%lf",&firstNumber);
    printf("\nEnter the second Number: ");
    scanf("%lf",&secondNumber);
    printf("\nChoose the operation:\n+ : for addition\n- : for subtraction\n* : for mulplication \n/ : for division\n");
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
        
        default:
            printf("invalid operation\n");
            return 0;
            break;
    }
    printf("final answer is %lf",ans);
}