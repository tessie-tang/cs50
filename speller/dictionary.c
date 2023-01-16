// Implements a dictionary's functionality
#include "dictionary.h"

#include <stdbool.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = 5400;

// Hash table
node *table[N];

// dictionary size
unsigned int dict_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int key = hash(word);

    node *bucket = table[key];
    while (bucket != NULL)
    {
        if (strcasecmp(bucket->word, word) == 0)
        {
            return true;
        }
        bucket = bucket->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long hash = N;
    int c;
    while ((c = tolower(*word++)))
    {
        hash = (hash << 4) + c + hash;
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char word[LENGTH + 1];
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    while (fscanf(dict, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n != NULL)
        {
            unsigned int key = hash(word);
            strcpy(n->word, word);
            n->next = table[key];
            table[key] = n;
            dict_size++;
        }
    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *bucket = table[i];
        while (bucket)
        {
            node *tmp = bucket;
            bucket = bucket->next;
            free(tmp);
        }

        if (i == N - 1 && bucket == NULL)
        {
            return true;
        }
    }
    return false;
}
