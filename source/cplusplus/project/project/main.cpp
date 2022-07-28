// IMPORT STANDARD LIBRARIES
#define BOOST_ALL_DYN_LINK
#include <iostream>
#include <string>
#include <ctype.h>
#include <boost/filesystem.hpp>
//#include <boost/algorithm/string.hpp>

// IMPORT THIRD-PARTY LIBRARIES
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/xform.h>
#include <pxr/usd/usdGeom/sphere.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/primrange.h>
#include <pxr/usd/usd/primCompositionQuery.h>


using namespace pxr;

void showVector(const std::vector<std::string>& old_paths)
{
    for (auto i : old_paths)
    {
        std::cout << i << std::endl;
    }
}

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

    for (int k = 0;k < layers.size();k++)
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


    std::vector<std::string> a = RemoveSubLayer(root_layer,usd_path);
    
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
        //modfiy path
        
        
        
        
        
        //
        i->GetReferences().ClearReferences();

        for (size_t t = 0; t < b.size(); t++)
            i->GetReferences().AddReference(GetRelPath(b[t],usd_path));

    }


    root_layer->SetSubLayerPaths(a);

    root_layer->Save();
    /*std::string out;
    root_layer->ExportToString(&out);
    std::cout << out<<std::endl;*/

}
int main() {
    
    const char* usd_path = "D:/test/test/layers2.usda";
    ModifyUsdFilePath(usd_path);


    /*auto stage = UsdStage::Open(usd_path);
    auto root_layer = stage->GetRootLayer();
    UsdPrimRange range = stage->TraverseAll();
    for (auto i = range.begin(); i != range.end(); ++i)
    {
        if (!i->HasAuthoredReferences()) continue;

        UsdPrimCompositionQuery layers_a = UsdPrimCompositionQuery::GetDirectReferences(*i);
        std::vector<UsdPrimCompositionQueryArc> layers = layers_a.GetCompositionArcs();

        for (size_t k = 0; k < layers.size(); ++k)
        {
            std::cout << layers[k].GetIntroducingLayer()->GetRealPath();
        }
    }*/
    std::cout << "hello world" << std::endl;
    std::cin.get();

    return 0;
}