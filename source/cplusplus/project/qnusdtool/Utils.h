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
void showVector(const std::vector<std::string>& old_paths);