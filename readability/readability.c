#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int get_readability_index(int num_letters, int num_words, int num_sentences) {
    float words_per_100 = num_words / 100.0;
    float l = num_letters / words_per_100;
    float s = num_sentences / words_per_100;
    return round(0.0588 * l - 0.296 * s - 15.8);
}

int main(void)
{
    string input = get_string("Text: ");

    int num_letters = 0;
    int num_words = 0;
    int num_sentences = 0;

    for (int i = 0; i < strlen(input); i++)
    {
        if (isalpha(input[i]))
        {
            num_letters++;
        }

        if (i > 0 && !isalpha(input[i]))
        {
            if (isalpha(input[i - 1]))
            {
                num_words++;
            }
        }

        int character = input[i];
        if (character == 46 || character == 33 || character == 63)
        {
            num_sentences ++;
        }
    }

    int readability_index = get_readability_index(num_letters, num_words, num_sentences);
    if (readability_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (readability_index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", readability_index);
    }
}
