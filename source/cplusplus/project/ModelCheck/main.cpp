// IMPORT STANDARD LIBRARIES
#include <iostream>
#include <string>
#include <vector>

// IMPORT THIRD-PARTY LIBRARIES
#include "../qnusdtool/modcheck.h"
#include "../qnusdtool/stagetool.h"
int main(int argc, const char** argv) {
    std::vector<AnimInfo*> a;
    AnimInfo* b0 = new AnimInfo();
    b0->anim_path = "./Elements_chuang_0.usd";
    b0->asset_path = "./Elements_chuang_mod.usd";
    b0->prim_path = "Elements_chuang_0";
    a.push_back(b0);

    const char* stage_path = "D:\\test\\e.usda";
    const char* all_usd[3] = { "D:\\test\\Elements_chuang_0.usd","D:\\test\\Elements_chuang_1.usd" ,"D:\\test\\Elements_chuang_2.usd" };
    /*std::cout << CreateAnimRef(a.size(),a.data(),stage_path) << std::endl;*/
    std::cout << CompositeLayer(3,all_usd,stage_path) << std::endl;
    return 0;
}