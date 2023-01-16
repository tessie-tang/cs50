#include "helpers.h"
#include <math.h>

int ceil_to_255(int color);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int r, g, b;
    float scale;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            b = image[i][j].rgbtBlue;
            scale = round((r + g + b) / 3.0);
            image[i][j].rgbtRed = scale;
            image[i][j].rgbtGreen = scale;
            image[i][j].rgbtBlue = scale;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int r, g, b;
    int sr, sg, sb;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            b = image[i][j].rgbtBlue;

            sr = round(0.393 * r + 0.769 * g + 0.189 * b);
            sg = round(0.349 * r + 0.686 * g + 0.168 * b);
            sb = round(0.272 * r + 0.534 * g + 0.131 * b);

            sr = ceil_to_255(sr);
            sg = ceil_to_255(sg);
            sb = ceil_to_255(sb);

            image[i][j].rgbtRed = sr;
            image[i][j].rgbtGreen = sg;
            image[i][j].rgbtBlue = sb;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE cache[width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            cache[j] = image[i][j];
        }

        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = cache[width - 1 - j].rgbtRed;
            image[i][j].rgbtGreen = cache[width - 1 - j].rgbtGreen;
            image[i][j].rgbtBlue = cache[width - 1 - j].rgbtBlue;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE cache[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            cache[h][w] = image[h][w];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int total_count = 0;
            float r_count = 0;
            float g_count = 0;
            float b_count = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (i + k < 0 || i + k >= height)
                    {
                        continue;
                    }

                    if (j + l < 0 || j + l >= width)
                    {
                        continue;
                    }

                    r_count += cache[i + k][j + l].rgbtRed;
                    g_count += cache[i + k][j + l].rgbtGreen;
                    b_count += cache[i + k][j + l].rgbtBlue;
                    total_count++;
                }
            }

            image[i][j].rgbtRed = (int)round(r_count / total_count);
            image[i][j].rgbtGreen = (int)round(g_count / total_count);
            image[i][j].rgbtBlue = (int)round(b_count / total_count);
        }
    }
}

int ceil_to_255(int color)
{
    if (color > 255)
    {
        return 255;
    }
    return color;
}