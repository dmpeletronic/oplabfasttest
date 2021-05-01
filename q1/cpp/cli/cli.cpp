#include <iostream>
#include <vector>
#include "../src/area.hpp"

void print_areas(std::vector<int> &areas)
{
    std::vector<int>::iterator it = areas.begin();
    std::cout << "[";
    for (auto it = begin(areas); it != end(areas); ++it) 
    {
        std::cout << *it;
        if (it == areas.end()-1)
        {
            std::cout << "]";
        }
        else
        {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;
}

int main(int argc, char **argv)
{
     // Check the number of parameters
    if (argc < 2) 
    {
        std::cerr << "Usage: " << argv[0] << " TotalArea" << std::endl;
        return 1;
    }
    // Get the parameter. We are not checking for format. It is just for manual testing.
    int totalArea =atoi(argv[1]);
    std::vector<int> list;
    farea(totalArea, list);
    print_areas(list);
    return 0;
}