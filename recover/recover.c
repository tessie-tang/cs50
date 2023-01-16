#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./recover image");
        return 1;
    }

    int buf_size = 512;
    FILE *card_file = fopen(argv[1], "r");
    unsigned char *buffer = malloc(buf_size);
    if (buffer == NULL)
    {
        return 1;
    }

    char *filename = malloc(12 * sizeof(char));
    int num_photo = 0;
    while (fread(buffer, sizeof(unsigned char), buf_size, card_file) == buf_size)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (num_photo == 1)
            {
                sprintf(filename, "%03i.jpg", num_photo);
                FILE *image = fopen(filename, "w");
                fwrite(buffer, 1, buf_size, image);
                fclose(image);
            }
            else
            {
                sprintf(filename, "%03i.jpg", num_photo);
                FILE *image = fopen(filename, "w");
                fwrite(buffer, 1, buf_size, image);
                fclose(image);
            }
            num_photo++;
        }
        else if (num_photo != 0)
        {
            FILE *image = fopen(filename, "a");
            fwrite(buffer, 1, buf_size, image);
            fclose(image);
        }
    }

    free(buffer);
    printf("contagem = %i\n", num_photo);
}