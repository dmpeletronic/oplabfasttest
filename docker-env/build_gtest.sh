#!/bin/bash
cd "/usr/src/gtest"
cmake CMakeLists.txt
make
# copy or symlink libgtest.a and libgtest_main.a to your /usr/lib folder
cp lib/*.a /usr/lib
