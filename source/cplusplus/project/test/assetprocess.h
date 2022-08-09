#pragma once
#include <string>
#include <vector>
bool GetAssetTexture_DLL(const char* usd_path, std::vector<std::string>& images);
bool PostProcessAsset_DLL(const char* usd_path, const char* asset_name);
