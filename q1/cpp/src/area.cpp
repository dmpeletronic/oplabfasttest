#include <iostream>
#include <vector>
#include <math.h>

/* 
 * Calculates the biggest square inside a given area 
 * \paran area: Input the area to find the biggest square
 * \return The area of the biggest square
 */
static int fit(int area)
{
    double square_side_length = sqrt(area);
    int truncated = (int)trunc(square_side_length);
    return truncated*truncated;
}

void farea(unsigned int area, std::vector<int>&squares)
{
    int remaining_area = area;
    while (remaining_area > 0)
    {
        // Calculate the biggest square for remaining area
        int result = fit(remaining_area);
#ifdef DEBUG
        std::cout << result << " ";
#endif
        // Add to square list
        squares.push_back(result);
        // And decrement the remaining area
        remaining_area -= result;
    }
#ifdef DEBUG
    std::cout << std::endl;
#endif
}
