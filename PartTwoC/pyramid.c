#include <stdio.h>

void draw(int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=i;j<n;j++)
            printf(" ");
        for(int j=i;j>0;j--)
            printf("*");
        for(int j=i;j>=0;j--)
            printf("*");
        printf("\n");
    }
}

void drawReversed(int n)
{
    for(int i=n;i>=0;i--)
    {
        for(int j=i;j<n;j++)
            printf(" ");
        for(int j=i;j>0;j--)
            printf("*");
        for(int j=i;j>=0;j--)
            printf("*");
        printf("\n");
    }
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("\n");
    if(n>0)
        draw(n);
    else if(n<0)
        drawReversed(-n);
    else
        printf("no pyramid exists with 0 m height");
}