#pragma once

#include "importlib.h"
#include <string>
#include <vector>
#include <sstream>

using std::string;
using std::vector;

struct AnimInfo
{
	const char* prim_path;
	const char* asset_path;
	const char* anim_path;
};

extern "C" {
	_declspec(dllexport) bool CreateAnimRef(int count, AnimInfo** infos, const char* path = "");
	_declspec(dllexport) bool CompositeLayer(int count, const char** infos, const char* path = "");
	_declspec(dllexport) bool CreateAnimLayer(int count, AnimInfo** infos, const char* path = "");
	_declspec(dllexport) bool CreateCFXLayer(int count, AnimInfo** infos, const char* path = "");
	_declspec(dllexport) void ModifyUsdFilePath(const char* usd_path);
}