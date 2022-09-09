#include <stdio.h>

char c;
int n;

void circle()
{
    n/=2;
    int l=n*1.5;
    for(int i=n;i>=-n;i-=2)
    {
        for(int j=-l;j<=l;j++)
        {
            if((i*i)+(j*j)==(n*n))printf("*");
            else printf(" ");
        }
        printf("\n");
    }
}

void square()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(!i || i==n-1 || !j || j==n-1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}

void pyramid()
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

void pyramidRevesed()
{
    n=-n;
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

void triangle()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<=i;j++)
            if(!j || j==i || i==n-1) printf("*");
            else printf(" ");
        printf("\n");
    }
}

void triangleReversed()
{
    n=-n;
    for(int i=n-1;i>=0;i--)
    {
        for(int j=0;j<=i;j++)
            if(!j || j==i || i==n-1) printf("*");
            else printf(" ");
        printf("\n");
    }
}

int main()
{
    printf("Enter desired shape then enter its dimension\n");
    scanf(" %c %d",&c,&n);
    switch (c)
    {
    case 'c':
        circle();
        break;
    case 'p':
        if(n>0)
            pyramid();
        else
            pyramidRevesed();
        break;
    case 't':
        if(n>0)
            triangle();
        else
            triangleReversed();
        break;
    case 's':
        square();
        break;
    default:
        break;
    }
}