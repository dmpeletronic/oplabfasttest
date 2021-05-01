#ifndef __AREA__
#define __AREA__
#include <vector>

/**
 * Function area
 * Calculates how many squares fits in a retangular window.
 * Receives the total area of the rectangle.
 * Generates a list/vector of squares area to fullfill the rectangle
 * Examples:
 *  Input: 15324
 *  Output 15129,169,25,1
 * 
 *  Input: 12
 *  Output 9, 1, 1, 1
 * 
 * \param area: Input param with total area of the rectangular window
 * \param squares: Output param as reference to an int vector with the squares areas 
 */ 
void farea(unsigned int area, std::vector<int>&squares);

#endif // __AREA__