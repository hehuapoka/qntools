#pragma once

#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif

#include <ctype.h>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/regex.hpp>

#include <iostream>
#include <string>
#include <vector>


#include "importlib.h"

std::string GetRelPath(std::string path, const std::string& layer_path);

template<typename T>
void showVector(const std::vector<T>& old_paths)
{
    for (auto i : old_paths)
    {
        std::cout << i << std::endl;
    }
}



template<typename T>
bool InVector(const std::vector<T>& old_paths,const T & a)
{
    for (auto& i : old_paths)
    {
        if (i == a) return true;
    }
    return false;
}


std::string GetShotAssetRelPath(std::string s_p, const std::string& layer_path);
//std::string GetRelReferencePath(const std::string& old_path, const std::string& layer_path);
std::vector<std::string> GetRelSublayerPathVector(const std::vector<std::string>& old_paths, const std::string layer_path);
void RemoveReferences(std::string primpath, std::vector<pxr::UsdPrimCompositionQueryArc>& layers, std::map<std::string, std::vector<std::string>>& reflayers);
std::vector<std::string> RemoveSubLayer(pxr::SdfLayerHandle layer, const std::string layer_path);