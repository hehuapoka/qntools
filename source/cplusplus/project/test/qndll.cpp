#include "qndll.h"
#include <wtypes.h>

typedef void(*GetAssetTexture)(const char* usd_path, std::vector<std::string>& images);
typedef void(*PostProcessAsset)(const char* usd_path, const char* asset_name);

static HMODULE module = LoadLibraryA(LPCSTR("qnusdtool.dll"));

bool GetAssetTexture_DLL(const char* usd_path, std::vector<std::string>& images)
{
	
	if (module != NULL)
	{
		GetAssetTexture a = (GetAssetTexture)GetProcAddress(module, LPCSTR("GetAssetTexture"));
		a(usd_path, images);
		return true;
	}
	else
	{
		return false;
	}
}

bool PostProcessAsset_DLL(const char* usd_path, const char* asset_name)
{
	//HMODULE module = LoadLibraryA(LPCSTR("qnusdtool.dll"));
	if (module != NULL)
	{
		PostProcessAsset a = (PostProcessAsset)GetProcAddress(module, LPCSTR("PostProcessAsset"));
		a(usd_path, asset_name);
		return true;
	}
	else
	{
		return false;
	}
}