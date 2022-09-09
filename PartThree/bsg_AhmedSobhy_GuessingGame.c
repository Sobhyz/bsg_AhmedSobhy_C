#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const int mod=1e3;

int main()
{
    int secretNumber=(rand()%mod) + 1;
    int guess;
    printf("Guess the Number: ");
    scanf("%d",&guess);
    while(guess!=secretNumber)
    {
        printf("Clue %c",((guess>secretNumber ? '>' : '<')));
        printf("\nguess again: ");
        scanf("%d",&guess);
    }
    printf("YOU WON!!");
}