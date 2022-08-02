#pragma once
#include "importlib.h"

using namespace pxr;

bool IsExistHierarchy(const std::string& path, UsdStageRefPtr stage);
bool InStringVector(const std::string& value, std::vector<std::string>& vec);
bool InUsdPrimsInVector(const std::string path, std::vector<std::string>& vec, UsdStageRefPtr stage);
bool IsOkayModHierarchy(UsdStageRefPtr stage);
bool IsOkayModTopology(UsdStageRefPtr stage, int minpoint = 4, int maxpoint = 4);

bool IsOkayAnimHierarchy(UsdStageRefPtr stage);

extern "C" {
    _declspec(dllexport) bool AssetModHierarchyCheck(const char* a);
    _declspec(dllexport) bool AssetModTopologyCheck(const char* a, int minpoint = 4, int maxpoint = 4);
    _declspec(dllexport) bool AssetModCheck(const char* a, int minpoint = 4, int maxpoint = 4);

    _declspec(dllexport) bool AssetAnimCheck(const char* a);
}

