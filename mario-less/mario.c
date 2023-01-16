#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = 0;
    int width = 0;
    while (height < 1 || height > 8)
    {
        height = get_int("Height: ");
        width = height;
    }

    for (int i = 1; i <= height; i++)
    {
        for (int j = 1; j <= width; j++)
        {
            if (j <= (width - i))
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}
