#define BOOST_ALL_DYN_LINK
// IMPORT STANDARD LIBRARIES
#include <iostream>
#include <string>
#include <vector>

#include <boost/filesystem.hpp>

#include "../qnusdtool/stagetool.h"
//
//void TestA()
//{
//    std::vector<AnimInfo*> a;
//    AnimInfo* b0 = new AnimInfo();
//    b0->anim_path = "./Elements_chuang_0.usd";
//    b0->asset_path = "./Elements_chuang_mod.usd";
//    b0->prim_path = "Elements_chuang_0";
//    a.push_back(b0);
//
//    AnimInfo* b1 = new AnimInfo();
//    b1->anim_path = "./Elements_chuang_1.usd";
//    b1->asset_path = "./Elements_chuang_mod.usd";
//    b1->prim_path = "Elements_chuang_1";
//    a.push_back(b1);
//
//    AnimInfo* b2 = new AnimInfo();
//    b2->anim_path = "./Elements_chuang_2.usd";
//    b2->asset_path = "./Elements_chuang_mod.usd";
//    b2->prim_path = "Elements_chuang_2";
//    a.push_back(b2);
//
//    const char* stage_path = "Z:/CGTeamWorkProject/Test1/USD/Shot/SC01/Shot001/Lighting/temp/SC01_Shot001_sets.usda";
//    const char* all_usd[3] = { "D:\\test\\Elements_chuang_0.usd","D:\\test\\Elements_chuang_1.usd" ,"D:\\test\\Elements_chuang_2.usd" };
//    /*std::cout << CreateAnimRef(a.size(),a.data(),stage_path) << std::endl;*/
//    //std::cout << CompositeLayer(3,all_usd,stage_path) << std::endl;
//    std::cout << CreateAnimLayer(a.size(), a.data(), stage_path) << std::endl;
//}
using namespace boost::filesystem;
int main(int argc, const char** argv) {
    PostProcessAsset("D:/test/test2/maya2.usda");
    std::cin.get();
    return 0;
}