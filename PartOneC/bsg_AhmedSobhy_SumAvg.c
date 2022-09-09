#include <stdio.h>

int main()
{
    double num1,num2,num3;
    printf("Enter first number: ");
    scanf("%lf",&num1);
    printf("\nEnter second number: ");
    scanf("%lf",&num2);
    printf("\nEnter third number: ");
    scanf("%lf",&num3);
    printf("sum of given numbers is: %lf\nAverage of given numbers is %lf",num1+num2+num3,((num1+num2+num3)/3));
}