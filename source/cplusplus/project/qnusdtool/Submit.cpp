#include "Submit.h"
#include "Utils.h"
#include "Modcheck.h"

using namespace pxr;
using std::cout;
using std::endl;

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

void RemoveReferences(std::string primpath, std::vector<UsdPrimCompositionQueryArc>& layers, std::map<std::string, std::vector<std::string>>& reflayers)
{
    for (int k = 0; k < layers.size(); k++)
    {
        auto l_a = layers[k].GetTargetNode().GetLayerStack()->GetLayers()[0];


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


    std::vector<std::string> a = RemoveSubLayer(root_layer, usd_path);

    // remove references
    UsdPrimRange range = stage->TraverseAll();
    for (auto i = range.begin(); i != range.end(); i++)
    {

        if (!i->HasAuthoredReferences()) continue;
        //RemoveReferences(prim);

        UsdPrimCompositionQuery layers_a = UsdPrimCompositionQuery::GetDirectReferences(*i);
        std::vector<UsdPrimCompositionQueryArc> layers = layers_a.GetCompositionArcs();
        if (layers.empty()) continue;

        RemoveReferences(i->GetPrimPath().GetAsString(), layers, reference_layers);
        i->GetReferences().ClearReferences();
    }


    //solver asset to relative
    
    range = stage->TraverseAll();
    for (auto i = range.begin(); i != range.end(); i++)
    {
        VtValue attr_value;
        std::map<std::string,std::string> need_modify_attr;
        UsdAttributeVector attrs = i->GetAttributes();
        for (auto attr = attrs.begin(); attr != attrs.end(); attr++)
        {
            std::string attr_type = attr->GetTypeName().GetCPPTypeName();
            if (attr_type == "SdfAssetPath")
            {
                attr->Get(&attr_value);
                if (attr_value.IsHolding<SdfAssetPath>())
                {
                    SdfAssetPath asset_path = SdfAssetPath(GetRelPath(attr_value.Get<SdfAssetPath>().GetResolvedPath(), usd_path));
                    attr->Set(asset_path);
                }
            }
            else if(attr_type == "std::string")
            {
                if (attr->GetName() == "inputs:filename")
                {
                    attr->Get(&attr_value);
                    std::string asset_path =GetRelPath(attr_value.Get<std::string>(), usd_path);

                    /*prim.RemoveProperty("inputs:filename")
                    filename = prim.CreateAttribute("inputs:filename", pxr.Sdf.ValueTypeNames.Asset)
                    filename.Set(old_file)*/

                    //attr->Set(asset_path);
                    need_modify_attr[attr->GetName().GetString()] = asset_path;
                }
            }
        }
        for (auto& ikk : need_modify_attr)
        {
            i->RemoveProperty(TfToken(ikk.first));
            UsdAttribute new_attr=i->CreateAttribute(TfToken(ikk.first), SdfValueTypeNames->Asset);
            new_attr.Set(SdfAssetPath(ikk.second));
        }
    }


    //reset references
    for (auto ref = reference_layers.begin(); ref != reference_layers.end(); ref++)
    {
        UsdPrim prim = stage->GetPrimAtPath(SdfPath(ref->first));
        for (std::string& ss : ref->second)
        {
            prim.GetReferences().AddReference(GetRelPath(ss, usd_path));
        }
    }



    //reset sublayer
    root_layer->SetSubLayerPaths(a);

    //save to dist
    root_layer->Save();
    /*std::string out;
    root_layer->ExportToString(&out);
    std::cout << out<<std::endl;*/

}