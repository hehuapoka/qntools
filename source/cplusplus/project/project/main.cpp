// IMPORT STANDARD LIBRARIES
#define BOOST_ALL_DYN_LINK
#include <iostream>
#include <string>
#include <map>
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
#include <pxr/usd/pcp/layerStack.h>


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

void RemoveReferences(std::string primpath,std::vector<UsdPrimCompositionQueryArc>& layers, std::map<std::string, std::vector<std::string>>& reflayers)
{
    for (int k = 0;k < layers.size();k++)
    {
        auto l_a=layers[k].GetTargetNode().GetLayerStack()->GetLayers()[0];


        reflayers[primpath].push_back(l_a->GetRealPath());
    }
}


void ModifyUsdFilePath(const char* usd_path)
{
    std::map<std::string, std::vector<std::string>> reference_layers;

    auto stage = UsdStage::Open(usd_path);
    //remove all sublayer
    auto root_layer = stage->GetRootLayer();
    stage->SetEditTarget(root_layer);


    std::vector<std::string> a = RemoveSubLayer(root_layer,usd_path);
    
    // remove references
    UsdPrimRange range = stage->TraverseAll();
    for (auto i = range.begin(); i != range.end(); i++)
    {
        
        if (!i->HasAuthoredReferences()) continue;
        //RemoveReferences(prim);

        UsdPrimCompositionQuery layers_a = UsdPrimCompositionQuery::GetDirectReferences(*i);
        std::vector<UsdPrimCompositionQueryArc> layers = layers_a.GetCompositionArcs();
        if (layers.empty()) continue;

        RemoveReferences(i->GetPrimPath().GetAsString(),layers,reference_layers);
        i->GetReferences().ClearReferences();
    }


    //solver asset to relative
    range = stage->TraverseAll();
    for (auto i = range.begin(); i != range.end(); i++)
    {
        VtValue attr_value;
        UsdAttributeVector attrs = i->GetAttributes();
        for (auto attr = attrs.begin(); attr != attrs.end(); attr++)
        {
            if (attr->GetTypeName().GetCPPTypeName() == "SdfAssetPath")
            {
                attr->Get(&attr_value);
                if (attr_value.IsHolding<SdfAssetPath>())
                {
                    SdfAssetPath asset_path = SdfAssetPath(GetRelPath(attr_value.Get<SdfAssetPath>().GetResolvedPath(), usd_path));
                    attr->Set(asset_path);
                }
            }           
        }
    }


    //reset references
    for (auto ref = reference_layers.begin(); ref != reference_layers.end(); ref++)
    {
        UsdPrim prim = stage->GetPrimAtPath(SdfPath(ref->first));
        for (std::string& ss : ref->second)
        {
            prim.GetReferences().AddReference(GetRelPath(ss,usd_path));
        }
    }



    //reset sublayer
    root_layer->SetSubLayerPaths(a);

    //save to dist
    //root_layer->Save();
    /*std::string out;
    root_layer->ExportToString(&out);
    std::cout << out<<std::endl;*/

}
int main() {
    
    const char* usd_path = "D:/test/test/grid.usd";
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
    std::cout << "\nhello world" << std::endl;
    std::cin.get();

    return 0;
}