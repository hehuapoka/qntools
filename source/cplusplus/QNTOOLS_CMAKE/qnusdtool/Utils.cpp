#include "Utils.h"
using namespace pxr;

std::string GetRelPath(std::string path, const std::string& layer_path)
{

    //boost::filesystem::path(layer_path).parent_path()
    std::string new_path = static_cast<char>(tolower(path[0])) + path.substr(1, path.size() - 1);
    std::string new_path_old = static_cast<char>(tolower(layer_path[0])) + layer_path.substr(1, layer_path.size() - 1);

    std::string solver_path = boost::filesystem::relative(new_path, boost::filesystem::path(new_path_old).parent_path()).string();
    if (solver_path.empty()) return path;
    boost::replace_all(solver_path, "\\", "/");

    return solver_path;
}


bool GetShotAssetRelPath(std::string s_p, std::string& o_p)
{
	using namespace boost;
	replace_all(s_p, "\\", "/");

	regex exp(".+(USD/[a-z]+/[a-z]+/[a-z]+/USD/[a-z]+_[a-z]+.\\usda)$", regex::icase);
	boost::smatch what;
	bool su = regex_match(s_p, what, exp, match_flag_type::match_perl);
	if (su)
	{
		o_p = std::string("../../../../") + what[1].str();
		return true;
	}
	return false;

}


//std::string GetRelReferencePath(const std::string& old_path, const std::string& layer_path)
//{
//	std::string n_p;
//	if (GetShotAssetRelPath(old_path, n_p))
//	{
//		return n_p;
//	}
//	else
//	{
//		return GetRelPath(old_path, layer_path);
//	}
//}

std::vector<std::string> GetRelSublayerPathVector(const std::vector<std::string>& old_paths, const std::string layer_path)
{
	std::vector<std::string> new_paths;
	std::string n_p;
	for (const std::string& p : old_paths)
	{
		if (GetShotAssetRelPath(p, n_p))
		{
			new_paths.push_back(n_p);
		}
		else
		{
			new_paths.push_back(GetRelPath(p, layer_path));
		}
	}
	return new_paths;
}




void RemoveReferences(std::string primpath, std::vector<UsdPrimCompositionQueryArc>& layers, std::map<std::string, std::vector<std::string>>& reflayers)
{
	for (int k = 0; k < layers.size(); k++)
	{
		auto l_a = layers[k].GetTargetNode().GetLayerStack()->GetLayers()[0];
		std::string str_n = l_a->GetRealPath();
		if (str_n.empty()) continue;
		reflayers[primpath].push_back(l_a->GetRealPath());
	}
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