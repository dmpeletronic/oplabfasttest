#include <gtest/gtest.h>
#include "../src/area.hpp"

TEST(AreaTestSuite, SimpleTest1) 
{
    std::vector<int> list;
    std::vector<int> expectedList{9, 1, 1, 1};
    farea(12, list);
    ASSERT_EQ(4, list.size());
    for (int i = 0; i < list.size(); ++i)
    {
        ASSERT_EQ(expectedList[i], list[i]);
    } 
}

TEST(AreaTestSuite, SimpleTest2) 
{
    std::vector<int> list;
    std::vector<int> expectedList{15129, 169, 25, 1};
    farea(15324, list);
    ASSERT_EQ(expectedList.size(), list.size());
    for (int i = 0; i < list.size(); ++i)
    {
        ASSERT_EQ(expectedList[i], list[i]);
    } 
}

TEST(AreaTestSuite, SimpleTest3) 
{
    std::vector<int> list;
    std::vector<int> expectedList{1000000};
    farea(1000000, list);
    ASSERT_EQ(expectedList.size(), list.size());
    for (int i = 0; i < list.size(); ++i)
    {
        ASSERT_EQ(expectedList[i], list[i]);
    } 
}

int main(int argc, char **argv) 
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}