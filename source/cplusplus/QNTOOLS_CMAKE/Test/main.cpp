#pragma once
//#include "stagetool.h"
#include <vector>
#include <string>
#include <iostream>
#include <map>
#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif
#include <Python.h>
int main(int argc,char** argv)
{
	Py_Initialize();
	PyRun_SimpleString("print(\"hello world\")\n");
	Py_Finalize();
	std::cin.get();
	return 0;
}