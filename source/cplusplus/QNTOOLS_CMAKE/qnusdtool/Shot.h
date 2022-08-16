#pragma once
#include "importlib.h"
#include <string>
#include <vector>
#include <sstream>
#include <map>

enum  USDTYPE
{
	ANIM = 0, CAM, MOV, SC
};

struct AnimCompositionInfo
{
	AnimCompositionInfo(USDTYPE u_t, std::string p_n, std::string ass_p, std::string anim_p)
	{
		usd_type = u_t;
		prim_name = p_n;
		asset_path = ass_p;
		anim_path = anim_p;
	}
	USDTYPE usd_type;
	std::string prim_name;
	std::string asset_path;
	std::string anim_path;
	bool use_normal;
};


extern "C" {
	//_declspec(dllexport) void CompositionAnimFiles(const std::vector<std::string>& files, std::vector<USDTYPE>& usd_type);
	_declspec(dllexport) void CompositionAnimFiles(const std::string file, USDTYPE usd_type, bool usd_normal = true);
	_declspec(dllexport) bool CreateShotAnimLayer(std::vector<AnimCompositionInfo>& infos, const char* path);
	_declspec(dllexport) void CreateShotAnimALLLayer(const std::string& path, const std::string& path2, const std::string& path3);
}
