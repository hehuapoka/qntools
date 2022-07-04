// IMPORT STANDARD LIBRARIES
#include <iostream>
#include <string>
#include <vector>

// IMPORT THIRD-PARTY LIBRARIES
#include "../qnusdtool/modcheck.h"
int main(int argc,const char** argv) {
    const char* stage_path = "D:\\test\\d.usd";
    std::cout << AssetModHierarchyCheck(stage_path) << std::endl;
    std::cout << AssetModTopologyCheck(stage_path) << std::endl;
    std::cout << AssetModCheck(stage_path,3,4) << std::endl;
    return 0;
}