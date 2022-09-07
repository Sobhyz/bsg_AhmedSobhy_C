#include <stdio.h>

const int maxLen=1e5+5;

int main()
{
    char game[4][maxLen];
    int rate;
    printf("Enter a name: ");
    scanf(" %[^\n]", game[0]);
    printf("\nEnter another name: ");
    scanf(" %[^\n]", game[1]);
    printf("\nEnter a color: ");
    scanf(" %[^\n]", game[2]);
    printf("\nEnter an adverb: ");
    scanf(" %[^\n]", game[3]);
    printf("\nEnter a number: ");
    scanf(" %d", &rate);
    printf("Once upon a time there was a developer named %s who struggled to solve a problem of %d rate",game[0],rate);
    printf("\nThe ballon of given problem had a %s color which was %s's favourite color",game[2],game[0]);
    printf("\nTherefor %s was called to solve this problem for %s and it ended %s.",game[1],game[0],game[3]);

}