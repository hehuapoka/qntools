#pragma once
#include "stagetool.h"
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <Shot.h>
#include <Utils.h>
#include <boost/algorithm/string.hpp>
#include <boost/regex.hpp>
#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif
//#include <Python.h>
int main(int argc,char** argv)
{
	using namespace boost;
	/*Py_Initialize();
	PyRun_SimpleString("print(\"hello world\")\n");
	Py_Finalize();*/
	std::vector<std::string> files;
	std::vector<USDTYPE> types;
	std::vector<std::string> his;

	files.push_back("E:\\Work\\test\\save\\Scene_Anim.usd");
	types.push_back(USDTYPE::SC);
	his.push_back("/main/root/geo/render");
	CompositionAnimFiles(files, types,his);

	//std::cout << su << std::endl;
	std::cin.get();
	return 0;
}