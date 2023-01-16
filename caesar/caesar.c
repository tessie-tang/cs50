#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // parse input
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (isalpha(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // encipher
    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext: ");
    encipher(plaintext, key);
}


int encipher(string plaintext, int key)
{
    char ci;
    int n = strlen(plaintext);
    char ciphertext[n];
    for (int i = 0; i < n; i++)
    {
        int c = plaintext[i];
        if (isalpha(c))
        {
            ci = c + key % 26;
            if (!(islower(ci) || isupper(ci)))
            {
                ci -= 26;
            }
        }
        else
        {
            ci = c;
        }
        ciphertext[i] = ci;
    }
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}