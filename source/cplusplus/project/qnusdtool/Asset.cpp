#include "modcheck.h"
#include "Asset.h"
#include "Utils.h"

using namespace pxr;
using std::cout;
using std::endl;
const std::vector<std::string> need_primvar = { 
    "arnold:autobump_visibility",
    "arnold:disp_autobump",
    "arnold:disp_height",
    "arnold:disp_padding",
    "arnold:disp_zero_value",
    "arnold:matte",
    "arnold:opaque",
    "arnold:smoothing",
    "arnold:subdiv_iterations",
    "arnold:subdiv_type",
};

bool IsNeedCopyPrimVar(std::string& name)
{
    for (auto& i : need_primvar)
    {
        if (i == name)
        {
            return true;
        }
    }
    return false;
}
template <typename T>
void AddXformMatrix(T& source_prim, T& dest_prim)
{
    GfMatrix4d local_matrix;
    VtValue vis_value;
    bool rest;
    bool a = source_prim.GetLocalTransformation(&local_matrix, &rest);

    if (a)
    {
        auto trans = dest_prim.AddTransformOp();
        trans.Set(local_matrix);
    }

    source_prim.GetVisibilityAttr().Get(&vis_value);
    if (vis_value.Get<TfToken>() == TfToken("invisible"))
        dest_prim.MakeInvisible();
}


void CopyPrimvars(UsdGeomMesh& source_prim, UsdGeomMesh& dest_prim)
{
    //SdfValueTypeNames
    for (auto &i : source_prim.GetPrimvars())
    {
        std::string attr_name = i.GetName();
        std::string attr_name_strip = UsdGeomPrimvar::StripPrimvarsName(TfToken(attr_name)).GetString();
        //attr_name_strip == "arnold:subdiv_iterations" || attr_name_strip == "arnold:subdiv_type" || attr_name_strip == "arnold:smoothing"
        if (!(attr_name_strip == "normals" || attr_name_strip.substr(0,2) == "st") && IsNeedCopyPrimVar(attr_name_strip))
        {
            VtValue value;
            if (i.Get(&value))
            {
                
                UsdGeomPrimvar attr=dest_prim.CreatePrimvar(TfToken(attr_name), i.GetTypeName(),i.GetInterpolation());
                attr.Set(value);

            }
        }
        if (attr_name_strip == "normals")
        {
            VtValue value;
            if (i.ComputeFlattened(&value))
            {
                UsdGeomPrimvar attr = dest_prim.CreatePrimvar(TfToken(attr_name_strip), i.GetTypeName(), UsdGeomTokens->faceVarying);
                //UsdGeomPrimvar attr = dest_prim.CreatePrimvar(TfToken(attr_name_strip), i.GetTypeName(), i.GetInterpolation());
                //dest_prim.GetNormalsAttr().Set(value);
                attr.Set(value);
            }
            
        }
        if(attr_name_strip.substr(0, 2) == "st")
        {
            VtValue value;
            if (i.ComputeFlattened(&value))
            {

                UsdGeomPrimvar attr = dest_prim.CreatePrimvar(TfToken(attr_name), i.GetTypeName(), i.GetInterpolation());
                attr.Set(value);

            }
        }
    }
}
//void CopyProps(UsdPrim& source_prim, UsdPrim& dest_prim)
//{
//    for()
//}
void CopySubsets(UsdGeomMesh& source_prim, UsdGeomMesh& dest_prim)
{
    UsdGeomImageable source_imageable(source_prim);
    UsdGeomImageable dest_imageable(dest_prim);
    std::vector<UsdGeomSubset> source_facesets=UsdGeomSubset::GetGeomSubsets(source_imageable, UsdGeomTokens->face);
    for (auto subset_it = source_facesets.begin(); subset_it != source_facesets.end(); subset_it++)
    {
        VtValue a;
        //std::cout << subset_it->GetPrim().GetName();
        if (subset_it->GetIndicesAttr().Get(&a))
        {
            UsdGeomSubset::CreateGeomSubset(dest_imageable, subset_it->GetPrim().GetName(), UsdGeomTokens->face, a.Get<VtIntArray>());
        }
        
        
    }

}
void PostProcessAssetMesh(UsdStageRefPtr stage, UsdGeomMesh& prim,bool use_normal=true)
{
    VtArray<GfVec3f> primvar;
    VtArray<GfVec3f> normal;
    VtArray<int> vertex_point;
    VtArray<int> vertex_prim;

    std::string new_path = prim.GetPrim().GetPrimPath().GetString();//GetRelPath(prim.GetPrim().GetPrimPath().GetString(), "/root/geo/render");
    UsdGeomMesh new_prim = UsdGeomMesh::Define(stage, SdfPath(new_path));

    AddXformMatrix<UsdGeomMesh>(prim, new_prim);
    //add attr
    UsdAttribute new_points = new_prim.CreatePointsAttr();
    UsdAttribute new_vertex_index = new_prim.CreateFaceVertexIndicesAttr();
    UsdAttribute new_vertex_faces = new_prim.CreateFaceVertexCountsAttr();


    //UsdGeomPrimvarsAPI::
    UsdAttribute points = prim.GetPointsAttr();//TfToken("points")
    
    if (points.Get(&primvar))
    {
        new_points.Set(primvar);
    }
    //vertex
    UsdAttribute vertex_index = prim.GetFaceVertexIndicesAttr();
    UsdAttribute vertex_faces = prim.GetFaceVertexCountsAttr();


    if (vertex_index.Get(&vertex_point))
    {
        new_vertex_index.Set(vertex_point);
    }
    if (vertex_faces.Get(&vertex_prim))
    {
        new_vertex_faces.Set(vertex_prim);
    }

    new_prim.GetPrim().GetAttribute(TfToken("subdivisionScheme")).Set(TfToken("none"));
    new_prim.GetPrim().GetAttribute(TfToken("doubleSided")).Set(true);
    //new_prim.CreateDisplayColorAttr();
    //new_prim.CreateDisplayOpacityAttr();
    //others st...
    CopyPrimvars(prim, new_prim);

    //create subsets
    CopySubsets(prim, new_prim);


}
void PostProcessAssetXform(UsdStageRefPtr stage, UsdGeomXform& prim)
{
    std::string new_path = prim.GetPrim().GetPrimPath().GetString();//GetRelPath(prim.GetPrim().GetPrimPath().GetString(), "/root/geo/render");
    UsdGeomXform new_prim = UsdGeomXform::Define(stage, SdfPath(new_path));

    AddXformMatrix<UsdGeomXform>(prim, new_prim);
}
void InitRenderStage(UsdStageRefPtr stage)
{
    UsdPrim root = stage->DefinePrim(SdfPath("/root"), TfToken("Xform"));
    UsdPrim root_geo = stage->DefinePrim(SdfPath("/root/geo"), TfToken("Scope"));
    UsdPrim root_simproxy = stage->DefinePrim(SdfPath("/root/simproxy"), TfToken("Scope"));

    UsdPrim root_geo_render = stage->DefinePrim(SdfPath("/root/geo/render"), TfToken("Scope"));
    UsdPrim root_geo_proxy = stage->DefinePrim(SdfPath("/root/geo/proxy"), TfToken("Scope"));

    //UsdPrim prim = stage->DefinePrim(SdfPath("/render"), TfToken("Scope"));
    UsdModelAPI(root).SetKind(TfToken("component"));
    stage->SetDefaultPrim(root);
    UsdGeomSetStageMetersPerUnit(stage, 0.01);
    UsdGeomSetStageUpAxis(stage, UsdGeomTokens->y);
}
bool PostProcessAssetRender(UsdStageRefPtr stageA, UsdStageRefPtr stageB)
{
    bool has_render = false;
    bool has_proxy = false;
    bool has_simproxy = false;
    //init
    InitRenderStage(stageB);

    //process render
    if (pxr::UsdPrim obj = stageA->GetPrimAtPath(pxr::SdfPath("/root/geo/render"))) {
        UsdPrimSubtreeRange prims = obj.GetAllDescendants();
        has_render = !prims.empty();

        for (auto prim = prims.begin(); prim != prims.end(); prim++)
        {
            UsdPrim temp = *prim;
            if (UsdGeomXform xform = UsdGeomXform(temp)) {

                PostProcessAssetXform(stageB, xform);
            }
            else if (UsdGeomMesh mesh = UsdGeomMesh(temp))
            {
                PostProcessAssetMesh(stageB, mesh);
            }
        }
    }


    //process proxy
    if (pxr::UsdPrim obj = stageA->GetPrimAtPath(pxr::SdfPath("/root/geo/proxy")))
    {
        UsdPrimSubtreeRange prims = obj.GetAllDescendants();
        has_proxy = !prims.empty();

        for (auto prim = prims.begin(); prim != prims.end(); prim++)
        {
            UsdPrim temp = *prim;
            if (UsdGeomXform xform = UsdGeomXform(temp)) {

                PostProcessAssetXform(stageB, xform);
            }
            else if (UsdGeomMesh mesh = UsdGeomMesh(temp))
            {
                PostProcessAssetMesh(stageB, mesh);
            }
        }
    }

    //process simproxy
    if (pxr::UsdPrim obj = stageA->GetPrimAtPath(pxr::SdfPath("/root/simproxy")))
    {
        UsdPrimSubtreeRange prims = obj.GetAllDescendants();
        has_simproxy = !prims.empty();

        for (auto prim = prims.begin(); prim != prims.end(); prim++)
        {
            UsdPrim temp = *prim;
            if (UsdGeomXform xform = UsdGeomXform(temp)) {

                PostProcessAssetXform(stageB, xform);
            }
            else if (UsdGeomMesh mesh = UsdGeomMesh(temp))
            {
                PostProcessAssetMesh(stageB, mesh);
            }
        }
    }

    //add proxy
    if (has_proxy)
    {
        UsdPrim render_prim = stageB->GetPrimAtPath(SdfPath("/root/geo/render"));
        UsdPrim proxy_prim = stageB->GetPrimAtPath(SdfPath("/root/geo/proxy"));
        //UsdPrim simproxy_prim = stageB->GetPrimAtPath(SdfPath("/root/simproxy"));
        UsdGeomScope(render_prim).CreatePurposeAttr(VtValue(UsdGeomTokens->render));
        UsdGeomScope(proxy_prim).CreatePurposeAttr(VtValue(UsdGeomTokens->proxy));

        UsdGeomScope(render_prim).SetProxyPrim(UsdGeomScope(proxy_prim));

    }
    if (has_simproxy)
    {
        UsdPrim root_prim = stageB->GetPrimAtPath(SdfPath("/root"));
        UsdPrim simproxy_prim = stageB->GetPrimAtPath(SdfPath("/root/simproxy"));
        UsdGeomScope(simproxy_prim).CreatePurposeAttr(VtValue(UsdGeomTokens->guide));
        UsdGeomScope(simproxy_prim).MakeInvisible();

        root_prim.CreateRelationship(TfToken("simproxy")).SetTargets(std::vector<SdfPath>{simproxy_prim.GetPrimPath()});


    }
    return has_render;
}
void CreateMaterialAndShader(UsdStageRefPtr stageA, UsdStageRefPtr stageB)
{
    UsdPrimSiblingRange prims = stageA->GetPrimAtPath(SdfPath("/")).GetAllChildren();
    for (auto prim = prims.begin(); prim != prims.end(); prim++)
    {
        TfToken type_name = prim->GetTypeName();
        if (type_name == TfToken("Material"))
        {
            //make mat
            SdfPath mtl_path = SdfPath(TfToken("/mtl" + prim->GetPrimPath().GetString()));
            UsdShadeMaterial new_material = UsdShadeMaterial::Define(stageB, mtl_path);

            //parm
            UsdShadeMaterial old_material = UsdShadeMaterial(*prim);
            std::vector<UsdShadeOutput> old_material_outputs = old_material.GetOutputs();
            for (auto& old_material_output : old_material_outputs)
            {
                new_material.CreateOutput(old_material_output.GetBaseName(), old_material_output.GetTypeName());
            }

            //make shader
            UsdPrimSubtreeRange shader_prims = prim->GetAllDescendants();
            for (auto shader_prim : shader_prims)
            {
                VtValue shader_id;

                std::string shader_s = shader_prim.GetPrimPath().GetString();
                SdfPath shader_path = SdfPath(TfToken("/mtl" + shader_prim.GetPrimPath().GetString()));

                UsdShadeShader old_shader = UsdShadeShader(shader_prim);
                UsdShadeShader new_shader = UsdShadeShader::Define(stageB, shader_path);

                old_shader.GetIdAttr().Get(&shader_id);
                new_shader.SetShaderId(shader_id.Get<TfToken>());

                std::vector<UsdShadeInput> shader_input_attrs = old_shader.GetInputs();
                for (auto& shader_input_attr : shader_input_attrs)
                {
                    if (shader_input_attr.GetBaseName() == TfToken("filename"))
                    {
                        new_shader.CreateInput(shader_input_attr.GetBaseName(), SdfValueTypeNames->Asset);
                    }
                    else
                    {
                        new_shader.CreateInput(shader_input_attr.GetBaseName(), shader_input_attr.GetTypeName());
                    }
                    
                }

                std::vector<UsdShadeOutput> shader_output_attrs = old_shader.GetOutputs();
                for (auto& shader_output_attr : shader_output_attrs)
                {
                    new_shader.CreateOutput(shader_output_attr.GetBaseName(), shader_output_attr.GetTypeName());
                }

            }
        }
    }
}
void ModifyMaterialAndShaderProps(UsdStageRefPtr stageA, UsdStageRefPtr stageB)
{
    UsdPrimRange prims=stageA->Traverse();
    for (auto prim = prims.begin(); prim != prims.end(); prim++)
    {
        TfToken type_name = prim->GetTypeName();
        if (type_name == TfToken("Material"))
        {
            SdfPath mtl_path = SdfPath(TfToken("/mtl" + prim->GetPrimPath().GetString()));
            UsdPrim new_prim=stageB->GetPrimAtPath(mtl_path);

            UsdShadeMaterial new_material = UsdShadeMaterial(new_prim);
            UsdShadeMaterial old_material=UsdShadeMaterial(*prim);

            std::vector<UsdShadeOutput> old_material_outputs=old_material.GetOutputs();
            for (auto& old_material_output : old_material_outputs)
            {
                
                std::vector<SdfPath> connect_source;
                old_material_output.GetRawConnectedSourcePaths(&connect_source);
                //
                //

                if (!connect_source.empty())
                {
                    //cout << connect_source[0] << endl;
                    SdfPath new_material_connect_path = SdfPath(TfToken("/mtl" + connect_source[0].GetString()));
                    new_material.GetOutput(old_material_output.GetBaseName()).ConnectToSource(new_material_connect_path);
                }
                        
            }
        }
        else if (type_name == TfToken("Shader"))
        {
            SdfPath mtl_path = SdfPath(TfToken("/mtl" + prim->GetPrimPath().GetString()));
            UsdPrim new_prim = stageB->GetPrimAtPath(mtl_path);

            UsdShadeShader new_shader = UsdShadeShader(new_prim);
            UsdShadeShader old_shader = UsdShadeShader(*prim);

            std::vector<UsdShadeInput> old_sahder_inputs = old_shader.GetInputs();
            for (auto& old_shader_input : old_sahder_inputs)
            {
                VtValue value;
                std::vector<SdfPath> connect_source;
                old_shader_input.GetRawConnectedSourcePaths(&connect_source);


                UsdAttribute old_attr=old_shader_input.GetAttr();
                old_attr.Get(&value);
                //new_shader.GetOutput(old_shader_input.GetBaseName()).GetAttr().Set(value);

                if (old_shader_input.GetBaseName() == TfToken("filename"))
                {
                    //这里有一个奇怪的bug
                    std::string moidify_udim = value.Get<std::string>();
                    boost::replace_first(moidify_udim, "<udim>", "<UDIM>");
                    new_prim.GetAttribute(old_attr.GetName()).Set(SdfAssetPath(moidify_udim));
                }
                else if(value.GetTypeName() != std::string("void"))
                {
                    new_prim.GetAttribute(old_attr.GetName()).Set(value);
                }

                if(!connect_source.empty())
                {
                    SdfPath new_shader_connect_path = SdfPath(TfToken("/mtl" + connect_source[0].GetString()));
                    //std::cout << old_shader.GetPath() <<"/" << old_shader_input.GetBaseName() << endl;
                    //std::cout << new_shader_connect_path << endl;
                    if (UsdProperty target_property=stageB->GetObjectAtPath(new_shader_connect_path).As<UsdProperty>())
                    {
                        new_shader.GetInput(old_shader_input.GetBaseName()).ConnectToSource(new_shader_connect_path);
                    }
                    else
                    {
                        //UsdPrim target_prim = stageB->GetPrimAtPath(new_shader_connect_path);
                        UsdShadeShader target_shader = UsdShadeShader::Get(stageB, new_shader_connect_path);
                        UsdShadeOutput target_shader_output=target_shader.CreateOutput(TfToken("out"),old_shader_input.GetTypeName());
                        new_shader.GetInput(old_shader_input.GetBaseName()).ConnectToSource(target_shader_output);
                    }
                    
                    
                }
            }
        }
    }
}
bool PostProcessAssetMtl(UsdStageRefPtr stageA, UsdStageRefPtr stageB)
{
    //init
    SdfPath mtl_path = SdfPath("/mtl");
    UsdGeomScope mtl_prim=UsdGeomScope::Define(stageB, mtl_path);
    stageB->SetDefaultPrim(mtl_prim.GetPrim());
    UsdGeomSetStageMetersPerUnit(stageB, 0.01);
    UsdGeomSetStageUpAxis(stageB, UsdGeomTokens->y);

    CreateMaterialAndShader(stageA, stageB);
    ModifyMaterialAndShaderProps(stageA, stageB);
    
}

void PostProcessAssetPayload(UsdStageRefPtr stageA, UsdStageRefPtr stageB)
{
    UsdGeomSetStageUpAxis(stageB, UsdGeomTokens->y);
    UsdGeomSetStageMetersPerUnit(stageB, 0.01);

    UsdPrim root_prim_payload = stageB->DefinePrim(SdfPath("/root"));
    UsdPrim mtl_prim_payload = stageB->DefinePrim(SdfPath("/root/mtl"));
    UsdModelAPI(root_prim_payload).SetKind(TfToken("component"));
    root_prim_payload.GetReferences().AddReference("./geo.usdc");
    mtl_prim_payload.GetReferences().AddReference("./mtl.usdc");
    stageB->SetDefaultPrim(root_prim_payload);

    //bind with mat
    UsdPrimRange prims = stageB->TraverseAll();
    for (auto prim = prims.begin(); prim != prims.end(); prim++)
    {
        TfToken type_name = prim->GetTypeName();
        if (type_name == TfToken("Mesh") || type_name == TfToken("GeomSubset"))
        {
            std::vector<SdfPath> old_mat_paths;
            UsdPrim old_prim = stageA->GetPrimAtPath(prim->GetPrimPath());
            old_prim.GetRelationship(TfToken("material:binding")).GetTargets(&old_mat_paths);
            
            if (!old_mat_paths.empty())
            {
                SdfPath mat_path = SdfPath("/root/mtl" + old_mat_paths[0].GetString());
                //cout << mat_path << endl;
                UsdShadeMaterial mat=UsdShadeMaterial::Get(stageB, mat_path);
                UsdShadeMaterialBindingAPI(*prim).Bind(mat);
            }
        }
    }
}

void PostProcessAsset(const char* usd_path, const char* asset_name)
{
    //step.0 make dir
    if (!boost::filesystem::exists("./asset"))
    {
        boost::filesystem::create_directory(asset_name);
    }
    //step.1 make geo.usdc
    std::stringstream out_geo_path;
    std::stringstream out_mtl_path;
    std::stringstream out_payload_path;
    std::stringstream out_asset_path;

    out_geo_path << "./" << asset_name << "/" << "geo" << ".usdc";
    out_mtl_path << "./" << asset_name << "/" << "mtl" << ".usdc";
    out_payload_path << "./" << asset_name << "/" << "payload" << ".usdc";
    out_asset_path << "./" << asset_name << "/" << asset_name << ".usda";
    boost::filesystem::path geo_path = boost::filesystem::path(usd_path).parent_path() / boost::filesystem::path(out_geo_path.str());
    boost::filesystem::path mtl_path = boost::filesystem::path(usd_path).parent_path() / boost::filesystem::path(out_mtl_path.str());
    boost::filesystem::path payload_path = boost::filesystem::path(usd_path).parent_path() / boost::filesystem::path(out_payload_path.str());
    boost::filesystem::path asset_path = boost::filesystem::path(usd_path).parent_path() / boost::filesystem::path(out_asset_path.str());

    auto stageA = UsdStage::Open(usd_path);


    auto stage_geo = UsdStage::CreateNew(geo_path.string());
    PostProcessAssetRender(stageA, stage_geo);
    stage_geo->GetRootLayer()->Save(true);

    //step.2 make mtl.usdc
    auto stage_mtl = UsdStage::CreateNew(mtl_path.string());
    PostProcessAssetMtl(stageA, stage_mtl);
    stage_mtl->GetRootLayer()->Save(true);

    //step.3 make payload
    auto stage_payload = UsdStage::CreateNew(payload_path.string());
    PostProcessAssetPayload(stageA, stage_payload);
    stage_payload->GetRootLayer()->Save(true);

    //step.4 make asset
    auto stage_asset = UsdStage::CreateNew(asset_path.string());
    UsdGeomSetStageUpAxis(stage_asset, UsdGeomTokens->y);
    UsdGeomSetStageMetersPerUnit(stage_asset, 0.01);

    UsdPrim root_prim_asset = stage_asset->DefinePrim(SdfPath("/root"),TfToken("Xform"));
    root_prim_asset.SetPayload(std::string("./payload.usdc"));

    stage_asset->SetDefaultPrim(root_prim_asset);
    stage_asset->GetRootLayer()->Save(true);
}