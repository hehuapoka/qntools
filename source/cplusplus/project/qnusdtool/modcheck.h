#pragma once
#include "importlib.h"

using namespace pxr;

extern "C" {
    _declspec(dllexport) bool AssetModHierarchyCheck(const char* a);
    _declspec(dllexport) bool AssetModTopologyCheck(const char* a, int minpoint = 4, int maxpoint = 4);
    _declspec(dllexport) bool AssetModCheck(const char* a, int minpoint = 4, int maxpoint = 4);

    _declspec(dllexport) bool AssetAnimCheck(const char* a);
}
bool IsExistHierarchy(const std::string& path, UsdStageRefPtr stage)
{
    bool ok = false;
    if (pxr::UsdObject obj = stage->GetObjectAtPath(pxr::SdfPath(path))) {
        if (pxr::UsdPrim prim = obj.As<pxr::UsdPrim>()) {
            ok = true;
        }
    }
    return ok;
}

bool InStringVector(const std::string& value, std::vector<std::string>& vec)
{
    bool ok = false;
    for (std::string s : vec)
    {
        if (s == value)
        {
            ok = true;
            break;
        }
    }
    return ok;
}
bool InUsdPrimsInVector(const std::string path, std::vector<std::string>& vec, UsdStageRefPtr stage)
{
    if (!IsExistHierarchy(path, stage) && path != "/")
        return true;

    UsdPrim prim = stage->GetPrimAtPath(SdfPath(path));
    int num = 0;
    for (auto value : prim.GetChildren())
    {
        if (!InStringVector(value.GetName().GetString(), vec))
        {
            return false;
        }
        num += 1;
    }
    if (num > vec.size())
        return false;
    return true;
}


bool IsOkayModHierarchy(UsdStageRefPtr stage)
{
    bool ok = true;
    std::vector<std::string> obj_c = { "root" };
    std::vector<std::string> obj_root_c = { "geo","simproxy","simcloth" };
    std::vector<std::string> obj_root_geo_c = { "render","proxy" };
    std::vector<std::string> obj_root_geo_proxy_c = { "main","hair","cloth" };
    std::vector<std::string> obj_root_geo_render_c = { "main","hair","cloth" };
    ok = ok && InUsdPrimsInVector("/", obj_c, stage);
    ok = ok && InUsdPrimsInVector("/root", obj_root_c, stage);
    ok = ok && InUsdPrimsInVector("/root/geo", obj_root_geo_c, stage);
    ok = ok && InUsdPrimsInVector("/root/geo/proxy", obj_root_geo_proxy_c, stage);
    /*ok = ok && InUsdPrimsInVector("/root/geo/render", obj_root_geo_render_c, stage);*/
    return ok;
}
bool IsOkayModTopology(UsdStageRefPtr stage,int minpoint = 4,int maxpoint = 4)
{
    UsdPrimRange usdrange = stage->Traverse();
    for (auto a = usdrange.begin();a != usdrange.end();a++)
    {
        TfToken prim_type = a->GetTypeName();
        if (prim_type == TfToken("Scope") || prim_type == TfToken("Xform") || prim_type == TfToken("Mesh"))
        {
            if (UsdGeomMesh mesh = UsdGeomMesh(*a))
            {
                UsdAttribute mesh_face_cout_attr = mesh.GetFaceVertexCountsAttr();
                VtIntArray mesh_face_cout;
                mesh_face_cout_attr.Get(&mesh_face_cout);
                //uint32_t cc = 0;
                for (auto fc = mesh_face_cout.begin(); fc != mesh_face_cout.end(); fc++)
                {
                    if (*fc < minpoint || *fc > maxpoint)
                    {
                        //std::cout << a->GetPrimPath() << "  --  "<<*fc << "  --  "<<cc<<std::endl;
                        return false;
                    }
                    //cc++;
                }
            }
        }
        else
        {
            return false;
        }
    }
    return true;
}


bool IsOkayAnimHierarchy(UsdStageRefPtr stage)
{
    bool ok = true;
    std::vector<std::string> obj_root_geo_render_c = { "main","hair","cloth" };

    std::vector<std::string> obj_c = { "render" };
    ok = ok && InUsdPrimsInVector("/", obj_c, stage);
    ok = ok && InUsdPrimsInVector("/render", obj_root_geo_render_c, stage);
    return ok;
}



