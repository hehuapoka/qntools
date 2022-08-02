#include "modcheck.h"
#include "Asset.h"
#include "Utils.h"

using namespace pxr;
using std::cout;
using std::endl;

void AddXformMatrix(UsdGeomXform& source_prim, UsdGeomXform& dest_prim)
{
    GfMatrix4d local_matrix;
    bool rest;
    bool a = source_prim.GetLocalTransformation(&local_matrix, &rest);

    if (a)
    {
        auto trans = dest_prim.AddTransformOp();
        trans.Set(local_matrix);
    }
}
void AddMeshMatrix(UsdGeomMesh& source_prim, UsdGeomMesh& dest_prim)
{
    GfMatrix4d local_matrix;
    bool rest;
    bool a = source_prim.GetLocalTransformation(&local_matrix, &rest);

    if (a)
    {
        auto trans = dest_prim.AddTransformOp();
        trans.Set(local_matrix);
    }
}
void PostProcessAssetMesh(UsdStageRefPtr stage, UsdGeomMesh& prim)
{
    VtArray<GfVec3f> primvar;
    VtArray<int> vertex_point;
    VtArray<int> vertex_prim;
    std::string new_path = prim.GetPrim().GetPrimPath().GetString();//GetRelPath(prim.GetPrim().GetPrimPath().GetString(), "/root/geo/render");
    UsdGeomMesh new_prim = UsdGeomMesh::Define(stage, SdfPath(new_path));

    AddMeshMatrix(prim, new_prim);

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


}
void PostProcessAssetXform(UsdStageRefPtr stage, UsdGeomXform& prim)
{
    std::string new_path = prim.GetPrim().GetPrimPath().GetString();//GetRelPath(prim.GetPrim().GetPrimPath().GetString(), "/root/geo/render");
    UsdGeomXform new_prim = UsdGeomXform::Define(stage, SdfPath(new_path));

    AddXformMatrix(prim, new_prim);
}
void InitRenderStage(UsdStageRefPtr stage)
{
    UsdPrim root = stage->DefinePrim(SdfPath("/root"), TfToken("Xform"));
    UsdPrim root_geo = stage->DefinePrim(SdfPath("/root/geo"), TfToken("Scope"));
    UsdPrim root_simproxy = stage->DefinePrim(SdfPath("/root/simproxy"), TfToken("Scope"));

    UsdPrim root_geo_render = stage->DefinePrim(SdfPath("/root/geo/render"), TfToken("Scope"));
    UsdPrim root_geo_proxy = stage->DefinePrim(SdfPath("/root/geo/proxy"), TfToken("Scope"));

    //UsdPrim prim = stage->DefinePrim(SdfPath("/render"), TfToken("Scope"));
}
bool PostProcessAssetRender(UsdStageRefPtr stageA, UsdStageRefPtr stageB)
{
    if (pxr::UsdPrim obj = stageA->GetPrimAtPath(pxr::SdfPath("/root/geo/render"))) {

        UsdPrimSubtreeRange prims = obj.GetAllDescendants();
        if (!prims.empty())
        {
            InitRenderStage(stageB);
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


            std::string out;
            stageB->ExportToString(&out);
            std::cout << out << std::endl;
        }

    }
    else {

        std::cout << "没有该路径" << std::endl;
    }
    return true;
}
void PostProcessAsset(const char* usd_path)
{
    boost::filesystem::path render_path = boost::filesystem::path(usd_path).parent_path() / boost::filesystem::path("render.usda");
    auto stageA = UsdStage::Open(usd_path);

    auto stageB = UsdStage::CreateNew(render_path.string());
    //stageB->SetEditTarget(stageB->GetRootLayer());

    PostProcessAssetRender(stageA, stageB);
    stageB->GetRootLayer()->Save(true);


}