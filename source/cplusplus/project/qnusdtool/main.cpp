#include "modcheck.h"
#include "stagetool.h"

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

bool AssetAnimCheck(const char* a)
{
    auto stage = UsdStage::Open(std::string(a), UsdStage::LoadAll);
    return IsOkayAnimHierarchy(stage);
}


bool CreateAnimRef(int count,AnimInfo ** infos,const char* path)
{
    try {
        auto stage = UsdStage::CreateNew(path);

        //´´½¨Default his
        auto root_sdfpath = SdfPath("/Anims");
        auto anims = UsdGeomXform::Define(stage, root_sdfpath);

        for (int i = 0; i < count; i++)
        {
            SdfPath sub_sdfpath = root_sdfpath.AppendChild(TfToken(infos[i]->prim_path));
            UsdPrim sub_xform = stage->DefinePrim(sub_sdfpath, TfToken("Xform"));

            UsdReferences ref = sub_xform.GetReferences();
            ref.AddReference(infos[i]->asset_path);

            UsdPrim anim_root =stage->OverridePrim(sub_sdfpath.AppendPath(SdfPath(TfToken("geo/render"))));
            anim_root.GetReferences().AddReference(infos[i]->anim_path);
        }
        stage->GetRootLayer()->Save();

        return true;

    }
    catch(std::exception& e)
    {
        return false;
    }
           
}
