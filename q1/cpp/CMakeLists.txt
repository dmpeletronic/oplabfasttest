cmake_minimum_required(VERSION 2.6)
 
# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
 
# Link unittest with what we want to test and the GTest and pthread library
add_executable(unittest test/test.cpp src/area.cpp)
target_link_libraries(unittest ${GTEST_LIBRARIES} pthread)

# Create CLI exceutable
add_executable(cli cli/cli.cpp src/area.cpp)