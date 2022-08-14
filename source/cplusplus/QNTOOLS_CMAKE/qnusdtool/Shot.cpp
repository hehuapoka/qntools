#include "Shot.h"
#include "Utils.h"
#include <iostream>
#include <boost/algorithm/string.hpp>
#include <boost/regex.hpp>

using namespace pxr;
void InitUSDLayer(pxr::UsdStageRefPtr stage, double start, double end,UsdPrim& default)
{
	UsdGeomSetStageUpAxis(stage, pxr::UsdGeomTokens->y);
	UsdGeomSetStageMetersPerUnit(stage, 0.01);
	stage->SetStartTimeCode(start);
	stage->SetEndTimeCode(end);
	stage->SetDefaultPrim(default);
}

template <typename T>
void AddShotXformMatrix(UsdStageRefPtr stage,T& source_prim, T& dest_prim)
{
    GfMatrix4d local_matrix;
    VtValue vis_value;
	VtValue xform;
    bool rest;
    
	std::vector<UsdGeomXformOp> xc =source_prim.GetOrderedXformOps(&rest);
	for (auto& ic : xc)
	{
		UsdGeomXformOp new_op = dest_prim.AddXformOp(ic.GetOpType(), ic.GetPrecision(), ic.GetOpName());
		
		if (ic.GetNumTimeSamples() > 1)
		{
			for (double t = stage->GetStartTimeCode(); t <= stage->GetEndTimeCode(); t++)
			{

				/*bool a = source_prim.GetLocalTransformation(&local_matrix, &rest, UsdTimeCode(t));
				if (a)
				{
					auto trans = dest_prim.AddTransformOp();
					trans.Set(local_matrix, UsdTimeCode(t));
				}*/
				if(ic.Get(&xform, UsdTimeCode(t)))
					new_op.Set(xform, UsdTimeCode(t));
			}
		}
		else
		{
			if (ic.Get(&xform))
				new_op.Set(xform);
			
		}
	}

    source_prim.GetVisibilityAttr().Get(&vis_value);
    if (vis_value.Get<TfToken>() == TfToken("invisible"))
        dest_prim.MakeInvisible();
}


void CopyShotPrimvars(UsdStageRefPtr stage,UsdGeomMesh& source_prim, UsdGeomMesh& dest_prim, bool use_normal = true)
{
    //SdfValueTypeNames
    for (auto& i : source_prim.GetPrimvars())
    {
        std::string attr_name = i.GetName();
        std::string attr_name_strip = UsdGeomPrimvar::StripPrimvarsName(TfToken(attr_name)).GetString();
		if (use_normal)
		{
			if (attr_name_strip == "normals")
			{
				VtValue value;
				UsdGeomPrimvar attr = dest_prim.CreatePrimvar(TfToken(attr_name_strip), i.GetTypeName(), UsdGeomTokens->faceVarying);

				for (double t = stage->GetStartTimeCode(); t <= stage->GetEndTimeCode(); t++)
				{
					UsdTimeCode _t = UsdTimeCode(t);

					if (i.ComputeFlattened(&value, _t))
					{
						attr.Set(value, _t);
					}
				}

			}
		}
        
        if (attr_name_strip.substr(0, 2) == "st")
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


void PostProcessShotMesh(UsdStageRefPtr old_stage ,UsdStageRefPtr stage, UsdGeomMesh& prim,const std::string& his,bool use_normal = true)
{
    VtArray<GfVec3f> primvar;
    VtArray<GfVec3f> extenvt;
    VtArray<int> vertex_point;
    VtArray<int> vertex_prim;

    std::string new_path = std::string("/") + GetRelPath(prim.GetPrim().GetPrimPath().GetString(), his);
    UsdGeomMesh new_prim = UsdGeomMesh::Define(stage, SdfPath(new_path));

    AddShotXformMatrix<UsdGeomMesh>(old_stage,prim, new_prim);
    //add attr
    UsdAttribute new_points = new_prim.CreatePointsAttr();
    UsdAttribute new_vertex_index = new_prim.CreateFaceVertexIndicesAttr();
    UsdAttribute new_vertex_faces = new_prim.CreateFaceVertexCountsAttr();
	UsdAttribute new_extent = new_prim.CreateExtentAttr();


    //UsdGeomPrimvarsAPI::
    UsdAttribute points = prim.GetPointsAttr();//TfToken("points")
    //vertex
    UsdAttribute vertex_index = prim.GetFaceVertexIndicesAttr();
    UsdAttribute vertex_faces = prim.GetFaceVertexCountsAttr();

	//UsdAttribute extent = prim.GetExtentAttr();

	if (vertex_index.Get(&vertex_point))
	{
		new_vertex_index.Set(vertex_point);
	}
	if (vertex_faces.Get(&vertex_prim))
	{
		new_vertex_faces.Set(vertex_prim);
	}

	
	for (double t = old_stage->GetStartTimeCode(); t <= old_stage->GetEndTimeCode();t++)
	{
		//std::cout << t << std::endl;
		UsdTimeCode _t = UsdTimeCode(t);
		if (points.Get(&primvar, _t))
		{
			new_points.Set(primvar, _t);
			prim.ComputeExtent(primvar, &extenvt);
			new_extent.Set(extenvt, _t);
		}
	}
	

    new_prim.GetPrim().GetAttribute(TfToken("subdivisionScheme")).Set(TfToken("none"));
    new_prim.GetPrim().GetAttribute(TfToken("doubleSided")).Set(true);

    CopyShotPrimvars(old_stage,prim, new_prim, use_normal);


}
void PostProcessShotXform(UsdStageRefPtr old_stage,UsdStageRefPtr stage, UsdGeomXform& prim, const std::string& his)
{
    std::string new_path = std::string("/")+GetRelPath(prim.GetPrim().GetPrimPath().GetString(), his);
	/*std::cout << new_path<<std::endl;*/
    UsdGeomXform new_prim = UsdGeomXform::Define(stage, SdfPath(new_path));

    AddShotXformMatrix<UsdGeomXform>(old_stage,prim, new_prim);
}


void CompositionAnimFiles_ANIM(std::string file,const std::string& his, bool use_normal=true)
{
	auto stageA = UsdStage::Open(file);
	std::string new_file = (boost::filesystem::path(".\\temp") / boost::filesystem::path(file).filename()).string();
	auto stageB = UsdStage::CreateNew(new_file);

	UsdPrim root_geo_render = stageB->DefinePrim(SdfPath("/render"), TfToken("Scope"));

	InitUSDLayer(stageB, stageA->GetStartTimeCode(), stageA->GetEndTimeCode(),root_geo_render);
	//render
	
	if (pxr::UsdPrim obj = stageA->GetPrimAtPath(pxr::SdfPath(his))) {
		UsdPrimSubtreeRange prims = obj.GetAllDescendants();
		for (auto prim = prims.begin(); prim != prims.end(); prim++)
		{
			UsdPrim temp = *prim;
			if (UsdGeomXform xform = UsdGeomXform(temp)) {

				PostProcessShotXform(stageA,stageB, xform,his);
			}
			else if (UsdGeomMesh mesh = UsdGeomMesh(temp))
			{
				PostProcessShotMesh(stageA,stageB, mesh,his,use_normal);
			}
		}
	}

	stageB->GetRootLayer()->Save();
}



void CompositionAnimFiles_CAM(std::string file)
{
	using namespace pxr;
	auto stage = UsdStage::Open(file);
	std::string new_file = (boost::filesystem::path(".\\temp") / boost::filesystem::path(file).filename()).string();
	auto stage_new = UsdStage::CreateNew(new_file);

	UsdPrim root = stage_new->DefinePrim(SdfPath("/cam"), TfToken("Xform"));

	InitUSDLayer(stage_new, stage->GetStartTimeCode(), stage->GetEndTimeCode(),root);

	UsdPrimRange prims = stage->Traverse();
	VtValue temp_value;
	for (auto prim = prims.begin(); prim != prims.end(); prim++)
	{
		if (prim->GetTypeName() == TfToken("Camera"))
		{
			UsdGeomCamera new_camera = UsdGeomCamera::Define(stage_new, SdfPath("/cam/camera"));
			if (UsdGeomCamera camera = UsdGeomCamera(*prim))
			{
				//copy no key value
				if (camera.GetClippingRangeAttr().Get(&temp_value))
					new_camera.GetClippingRangeAttr().Set(temp_value);
				if (camera.GetClippingPlanesAttr().Get(&temp_value))
					new_camera.GetClippingPlanesAttr().Set(temp_value);

				UsdAttribute old_focal = camera.GetFocalLengthAttr();
				UsdAttribute new_focal = new_camera.GetFocalLengthAttr();
				if (camera.GetFocalLengthAttr().GetNumTimeSamples() > 1)
				{
					for (double t = stage->GetStartTimeCode(); t <= stage->GetEndTimeCode();)
					{
						t = t + 1.0;
						if (old_focal.Get(&temp_value, UsdTimeCode(t)))
							new_focal.Set(temp_value, UsdTimeCode(t));
					}
				}
				else
				{
					if (old_focal.Get(&temp_value))
						new_focal.Set(temp_value);
				}

				if (camera.GetFocusDistanceAttr().Get(&temp_value))
					new_camera.GetFocusDistanceAttr().Set(temp_value);
				if (camera.GetVerticalApertureAttr().Get(&temp_value))
					new_camera.GetVerticalApertureAttr().Set(temp_value);
				if (camera.GetHorizontalApertureAttr().Get(&temp_value))
					new_camera.GetHorizontalApertureAttr().Set(temp_value);

				if (camera.GetVerticalApertureOffsetAttr().Get(&temp_value))
					new_camera.GetVerticalApertureOffsetAttr().Set(temp_value);
				if (camera.GetHorizontalApertureOffsetAttr().Get(&temp_value))
					new_camera.GetHorizontalApertureOffsetAttr().Set(temp_value);

				//copy key value
				UsdGeomXformOp x = new_camera.AddTransformOp();
				for (double t = stage->GetStartTimeCode(); t <= stage->GetEndTimeCode();)
				{
					t = t + 1.0;
					GfMatrix4d m = camera.ComputeLocalToWorldTransform(UsdTimeCode(t));
					x.Set(m, UsdTimeCode(t));
				}
				
			}
			

			break;
		}

	}
	stage_new->GetRootLayer()->Save();
}
//-------------------



void CompositionAnimFiles_SC(std::string file)
{
		//copy
	if (!boost::filesystem::exists(file))
		return;
	boost::filesystem::path pp = boost::filesystem::path("temp") / boost::filesystem::path(file).filename();
	pp=boost::filesystem::absolute(pp);
	boost::filesystem::copy_file(file, pp, boost::filesystem::copy_option::overwrite_if_exists);

	std::map<std::string, std::vector<std::string>> reference_layers;

	auto stage = UsdStage::Open(pp.string());
	//remove all sublayer
	auto root_layer = stage->GetRootLayer();
	stage->SetEditTarget(root_layer);


	std::vector<std::string> a = RemoveSubLayer(root_layer, file);

	// remove references
	UsdPrimRange range = stage->TraverseAll();
	for (auto i = range.begin(); i != range.end(); i++)
	{

		if (!i->HasAuthoredReferences()) continue;
		//RemoveReferences(prim);

		UsdPrimCompositionQuery layers_a = UsdPrimCompositionQuery::GetDirectRootLayerArcs(*i);
		std::vector<UsdPrimCompositionQueryArc> layers = layers_a.GetCompositionArcs();
		if (layers.empty()) continue;

		RemoveReferences(i->GetPrimPath().GetAsString(), layers, reference_layers);
		i->GetReferences().ClearReferences();
	}

	//reset references
	std::string n_p;

	for (auto ref = reference_layers.begin(); ref != reference_layers.end(); ref++)
	{
		UsdPrim prim = stage->GetPrimAtPath(SdfPath(ref->first));

		for (std::string& ss : ref->second)
		{
			if (GetShotAssetRelPath(ss, n_p))
			{
				prim.GetReferences().AddReference(n_p);
			}
			else
			{
				//std::cout << GetRelPath(ss, pp.string()) << std::endl << ss << std::endl<< pp.string() <<std::endl;
				prim.GetReferences().AddReference(GetRelPath(ss, pp.string()));
			}
		}
	}

	root_layer->SetSubLayerPaths(a);
	root_layer->Save();

}
void CompositionAnimFiles(const std::vector<std::string>& files, std::vector<USDTYPE>& usd_type,const std::vector<std::string>& his)
{
	if (!boost::filesystem::exists(".\\temp"))
		boost::filesystem::create_directory("temp");

	for (int f = 0; f < files.size(); f++)
	{
		if (usd_type[f] == USDTYPE::ANIM)
		{
			CompositionAnimFiles_ANIM(files[f],his[f],false);
		}
		else if (usd_type[f] == USDTYPE::CAM)
		{
			CompositionAnimFiles_CAM(files[f]);
		}
		else if (usd_type[f] == USDTYPE::SC)
		{
			CompositionAnimFiles_SC(files[f]);
		}
	}
	
}