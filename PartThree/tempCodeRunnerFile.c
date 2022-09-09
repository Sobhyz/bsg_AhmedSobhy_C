for(int i=0;i<n;i++)
    {
        for(int j=0;j<=i;j++)
            if(!j || j==i || i==n-1) printf("*");
            else printf(" ");
        printf("\n");
    }