#pragma once

#include "importlib.h"
#include <string>
#include <vector>
#include <sstream>
#include <map>

extern "C" {
	_declspec(dllexport) void PostProcessAsset(const char* usd_path, const char* asset_name);
	//_declspec(dllexport) void GetAssetTexture(const char* usd_path,std::vector<std::string>& images,std::vector<std::string>& colorspace);
	_declspec(dllexport) void GetAssetTexture(const char* usd_path,std::map<std::string,std::string> & images);
}
