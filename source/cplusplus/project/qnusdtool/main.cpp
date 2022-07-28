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
            UsdPrim sub_xform = stage->DefinePrim(sub_sdfpath);

            UsdReferences ref = sub_xform.GetReferences();
            ref.AddReference(infos[i]->asset_path);

            /*UsdPrim anim_root =stage->OverridePrim(sub_sdfpath.AppendPath(SdfPath(TfToken("geo/render"))));
            anim_root.GetReferences().AddReference(infos[i]->anim_path);*/
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
            if (TfToken(infos[i]->prim_path) == TfToken("Cameras"))
            {
                SdfPath sub_sdfpath = root_sdfpath.AppendChild(TfToken(infos[i]->prim_path));
                SdfPath render_sdfpath = sub_sdfpath.AppendChild(TfToken("Main"));

                UsdPrim sub_xform = stage->DefinePrim(sub_sdfpath, TfToken("Xform"));
                UsdPrim render_xform = stage->DefinePrim(render_sdfpath);

                render_xform.GetReferences().AddReference(infos[i]->anim_path);
            }
            else
            {
                SdfPath sub_sdfpath = root_sdfpath.AppendChild(TfToken(infos[i]->prim_path));
                SdfPath geo_sdfpath = sub_sdfpath.AppendChild(TfToken("geo"));
                SdfPath render_sdfpath = geo_sdfpath.AppendChild(TfToken("render"));

                UsdPrim sub_xform = stage->DefinePrim(sub_sdfpath, TfToken("Xform"));
                UsdPrim geo_xform = stage->DefinePrim(geo_sdfpath, TfToken("Xform"));
                UsdPrim render_xform = stage->DefinePrim(render_sdfpath);

                render_xform.GetReferences().AddReference(infos[i]->anim_path);
            }
            
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
            UsdPrim render_xform = stage->DefinePrim(render_sdfpath);

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


////////////////////这里是重新解算路径

//void showVector(const std::vector<std::string>& old_paths)
//{
//    for (auto i : old_paths)
//    {
//        std::cout << i << std::endl;
//    }
//}

std::string GetRelPath(std::string path, const std::string& layer_path)
{

    //boost::filesystem::path(layer_path).parent_path()
    std::string new_path = static_cast<char>(tolower(path[0])) + path.substr(1, path.size() - 1);
    std::string new_path_old = static_cast<char>(tolower(layer_path[0])) + layer_path.substr(1, layer_path.size() - 1);

    std::string solver_path = boost::filesystem::relative(new_path, boost::filesystem::path(new_path_old).parent_path()).string();
    if (solver_path.empty()) return path;

    return solver_path;
}
std::vector<std::string> GetRelSublayerPathVector(const std::vector<std::string>& old_paths, const std::string layer_path)
{
    std::vector<std::string> new_paths;
    for (const std::string& p : old_paths)
    {
        new_paths.push_back(GetRelPath(p, layer_path));
    }
    return new_paths;
}

std::vector<std::string> RemoveSubLayer(SdfLayerHandle layer, const std::string layer_path)
{
    std::vector<std::string> name_layers = layer->GetSubLayerPaths();
    size_t num_sublayer = layer->GetNumSubLayerPaths();
    for (int i = 0; i < num_sublayer; i++)
    {
        layer->RemoveSubLayerPath(i);
    }

    return GetRelSublayerPathVector(name_layers, layer_path);
}

std::vector<std::string> RemoveReferences(std::vector<UsdPrimCompositionQueryArc>& layers)
{
    std::vector<std::string> reflayers;

    for (int k = 0; k < layers.size(); k++)
    {
        reflayers.push_back(layers[k].GetIntroducingLayer()->GetRealPath());
    }

    return reflayers;
}


void ModifyUsdFilePath(const char* usd_path)
{

    auto stage = UsdStage::Open(usd_path);
    //remove all sublayer
    auto root_layer = stage->GetRootLayer();


    std::vector<std::string> a = RemoveSubLayer(root_layer, usd_path);

    UsdPrimRange range = stage->TraverseAll();
    for (auto i = range.begin(); i != range.end(); i++)
    {
        if (!i->HasAuthoredReferences()) continue;
        UsdPrim prim = *i;
        //RemoveReferences(prim);

        UsdPrimCompositionQuery layers_a = UsdPrimCompositionQuery::GetDirectReferences(*i);
        std::vector<UsdPrimCompositionQueryArc> layers = layers_a.GetCompositionArcs();

        if (layers.empty()) continue;

        std::vector<std::string> b = RemoveReferences(layers);

        i->GetReferences().ClearReferences();

        for (size_t t = 0; t < b.size(); t++)
            i->GetReferences().AddReference(GetRelPath(b[t], usd_path));

    }


    root_layer->SetSubLayerPaths(a);

    root_layer->Save();
    /*std::string out;
    root_layer->ExportToString(&out);
    std::cout << out<<std::endl;*/

}