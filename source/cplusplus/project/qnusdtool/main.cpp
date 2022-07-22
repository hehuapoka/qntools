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

        //创建Default his
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


bool CreateAnimLayer(int count, AnimInfo** infos, const char* path)
{
    try {
        auto stage = UsdStage::CreateNew(path);

        //创建Default his
        auto root_sdfpath = SdfPath("/Anims");
        auto anims = UsdGeomXform::Define(stage, root_sdfpath);

        for (int i = 0; i < count; i++)
        {
            SdfPath sub_sdfpath = root_sdfpath.AppendChild(TfToken(infos[i]->prim_path));
            SdfPath geo_sdfpath = sub_sdfpath.AppendChild(TfToken("geo"));
            SdfPath render_sdfpath = geo_sdfpath.AppendChild(TfToken("render"));

            UsdPrim sub_xform = stage->DefinePrim(sub_sdfpath, TfToken("Xform"));
            UsdPrim geo_xform = stage->DefinePrim(geo_sdfpath, TfToken("Xform"));
            UsdPrim render_xform = stage->DefinePrim(render_sdfpath, TfToken("Xform"));

            render_xform.GetReferences().AddReference(infos[i]->anim_path);
        }
        stage->GetRootLayer()->Save();

        return true;

    }
    catch (std::exception& e)
    {
        return false;
    }

}
bool CreateCFXLayer(int count, AnimInfo** infos, const char* path)
{
    try {
        auto stage = UsdStage::CreateNew(path);

        //创建Default his
        auto root_sdfpath = SdfPath("/Anims");
        auto anims = UsdGeomXform::Define(stage, root_sdfpath);

        for (int i = 0; i < count; i++)
        {
            SdfPath sub_sdfpath = root_sdfpath.AppendChild(TfToken(infos[i]->prim_path));
            SdfPath geo_sdfpath = sub_sdfpath.AppendChild(TfToken("geo"));
            SdfPath render_sdfpath = geo_sdfpath.AppendChild(TfToken("render"));

            UsdPrim sub_xform = stage->DefinePrim(sub_sdfpath, TfToken("Xform"));
            UsdPrim geo_xform = stage->DefinePrim(geo_sdfpath, TfToken("Xform"));
            UsdPrim render_xform = stage->DefinePrim(render_sdfpath, TfToken("Xform"));

            render_xform.GetReferences().AddReference(infos[i]->anim_path);
        }
        stage->GetRootLayer()->Save();

        return true;

    }
    catch (std::exception& e)
    {
        return false;
    }

}

bool CompositeLayer(int count, const char** infos,const char* path)
{
    try {
        auto stage = UsdStage::CreateNew(path);

        //add sublayer
        


        for (int i = 0; i < count; i++)
        {
            stage->GetRootLayer()->InsertSubLayerPath(TfToken(infos[i]));
        }
        stage->GetRootLayer()->Save();

        return true;

    }
    catch (std::exception& e)
    {
        return false;
    }

}
