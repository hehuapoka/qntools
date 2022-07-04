#include "modcheck.h"

using namespace pxr;
using std::cout;

bool AssetModHierarchyCheck(const char *a)
{
    auto stage = UsdStage::Open(std::string(a), UsdStage::LoadAll);
    return IsOkayModHierarchy(stage);
}
bool AssetModTopologyCheck(const char* a,int minpoint,int maxpoint)
{
    auto stage = UsdStage::Open(std::string(a), UsdStage::LoadAll);
    return IsOkayModTopology(stage,minpoint,maxpoint);
}

bool AssetModCheck(const char* a, int minpoint, int maxpoint)
{
    auto stage = UsdStage::Open(std::string(a), UsdStage::LoadAll);
    return IsOkayModHierarchy(stage) && IsOkayModTopology(stage, minpoint, maxpoint);
}