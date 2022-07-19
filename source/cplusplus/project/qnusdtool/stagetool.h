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
}

//vector<string> split(string s, char token) {
//	std::stringstream iss(s);
//	string word;
//	vector<string> vs;
//	while (std::getline(iss, word, token)) {
//		vs.push_back(word);
//	}
//	return vs;
//}