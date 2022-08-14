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

extern "C" {
	_declspec(dllexport) void CompositionAnimFiles(const std::vector<std::string>& files, std::vector<USDTYPE>& usd_type, const std::vector<std::string>& his);
}
