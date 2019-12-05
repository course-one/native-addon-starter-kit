/*
 * A C++ program to test `src/greeting.cpp` file.
 * 
 * Command:
 * $ g++ greeting_test.cpp ../src/greeting.cpp -o greeting_test.exe
 */

#include <iostream>
#include <string>
#include "../src/greeting.h"

int main() {
    std::string result = helloUser( "John" );

    std::cout << result << std::endl;
}