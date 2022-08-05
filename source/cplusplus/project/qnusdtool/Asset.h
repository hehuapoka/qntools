#pragma once

#include "importlib.h"
#include <string>
#include <vector>
#include <sstream>

extern "C" {
	_declspec(dllexport) void PostProcessAsset(const char* usd_path, const char* asset_name);
}