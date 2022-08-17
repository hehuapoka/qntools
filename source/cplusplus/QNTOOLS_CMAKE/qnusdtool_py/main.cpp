#pragma once

#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif

#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <Shot.h>
#include <boost/python.hpp>

namespace bpy = boost::python;

template <typename Container>
bpy::list stl2py(const Container& vec) {
  typedef typename Container::value_type T;
  bpy::list lst;
  std::for_each(vec.begin(), vec.end(), [&](const T& t) { lst.append(t); });
  return lst;
}

template <typename Container>
void py2stl(const bpy::list& lst, Container& vec) {
  typedef typename Container::value_type T;
  bpy::stl_input_iterator<T> beg(lst), end;
  std::for_each(beg, end, [&](const T& t) { vec.push_back(t); });
}
void ConvertShotUSD(const std::string& path, USDTYPE type, bool normal=true)
{
	//std::cout << normal << std::endl;
	CompositionAnimFiles(path, type, normal);
}

void ConvertShotAnimLayer(const bpy::list& lhs,const char* usd_path)
{
	//std::cout << normal << std::endl;
	std::vector<AnimCompositionInfo> out_vec;
	py2stl(lhs, out_vec);
	CreateShotAnimLayer(out_vec, usd_path);
}

void ConvertShotCfxLayer(const bpy::list& lhs, const char* usd_path)
{
	//std::cout << normal << std::endl;
	std::vector<AnimCompositionInfo> out_vec;
	py2stl(lhs, out_vec);
	CreateShotCfxLayer(out_vec, usd_path);
}



BOOST_PYTHON_MODULE(qnusdtool_py)

{
	using namespace boost::python;
	//ANIM = 0, CAM, MOV, SC
	enum_<USDTYPE>("USDTYPE")
		.value("ANIM", ANIM)
		.value("CAM", CAM)
		.value("MOV", MOV)
		.value("SC", SC)
		;
	class_<AnimCompositionInfo>("AnimCompositionInfo", init<USDTYPE, std::string, std::string, std::string>())
		.def_readonly("usd_type", &AnimCompositionInfo::usd_type)
		.def_readonly("prim_name", &AnimCompositionInfo::prim_name)
		.def_readonly("asset_path", &AnimCompositionInfo::asset_path)
		.def_readonly("anim_path", &AnimCompositionInfo::anim_path)
		;
	def("ConvertShotUSD", ConvertShotUSD);
	def("ConvertShotAnimLayer", ConvertShotAnimLayer);
	def("ConvertShotCfxLayer", ConvertShotCfxLayer);
	def("CreateShotAnimALLLayer", CreateShotAnimALLLayer);
}
