// IMPORT STANDARD LIBRARIES
#include <iostream>
#include <string>
#include <vector>

// IMPORT THIRD-PARTY LIBRARIES
#include "../qnusdtool/modcheck.h"
int main(int argc,const char** argv) {
    const char* stage_path = "D:\\test\\e.usd";
    std::cout << AssetAnimCheck(stage_path) << std::endl;
    return 0;
}