// IMPORT STANDARD LIBRARIES
#include <iostream>
#include <string>

// IMPORT THIRD-PARTY LIBRARIES
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/xform.h>
#include <pxr/usd/usdGeom/sphere.h>


int main() {
    auto stage = pxr::UsdStage::CreateNew("hello.usda");
    auto xform =pxr::UsdGeomXform::Define(stage, pxr::SdfPath("/root"));

    auto sphere = pxr::UsdGeomSphere::Define(stage, pxr::SdfPath("/root/sphre"));
    
    //sphre 
    auto r = sphere.GetRadiusAttr();
    r.Set(2.0);

    stage->GetRootLayer()->Save();

    return 0;
}