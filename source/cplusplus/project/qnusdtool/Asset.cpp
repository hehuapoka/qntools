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
void CopySubsets(UsdGeomMesh& source_prim, UsdGeomMesh& dest_prim)
{
    UsdGeomImageable source_imageable(source_prim);
    std::vector<UsdGeomSubset> source_facesets=UsdGeomSubset::GetGeomSubsets(source_imageable, UsdGeomTokens->face);
    for (auto subset_it = source_facesets.begin(); subset_it != source_facesets.end(); subset_it++)
    {
        std::cout << subset_it->GetPrim().GetName();
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
    stage->SetDefaultPrim(root);
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
            /*else if(prim->GetTypeName() == TfToken("GeomSubset"))
            {
                
            }*/
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
    return has_render;
}

void PostProcessAsset(const char* usd_path)
{
    boost::filesystem::path geo_path = boost::filesystem::path(usd_path).parent_path() / boost::filesystem::path("geo.usdc");
    auto stageA = UsdStage::Open(usd_path);

    auto stageB = UsdStage::CreateNew(geo_path.string());
    //stageB->SetEditTarget(stageB->GetRootLayer());

    PostProcessAssetRender(stageA, stageB);
    stageB->GetRootLayer()->Save(true);

    /*std::string out;
    stageB->ExportToString(&out);
    std::cout << out << std::endl;*/
}