#pragma once

#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif

#include <ctype.h>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>

#include <iostream>
#include <string>
#include <vector>


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