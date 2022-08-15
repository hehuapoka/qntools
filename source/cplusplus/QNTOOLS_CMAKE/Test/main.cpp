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

	CompositionAnimFiles("D:\\test\\temp\\Anim\\Chars_ak_1.usd", USDTYPE::ANIM,true);

	//std::cout << su << std::endl;
	std::cin.get();
	return 0;
}