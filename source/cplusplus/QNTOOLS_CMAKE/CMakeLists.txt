# CMakeList.txt: 顶层 CMake 项目文件，在此处执行全局配置
# 并包含子项目。
#
cmake_minimum_required (VERSION 3.8)

project ("QNTOOLS_CMAKE")

set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}")
set(EXECUTABLE_OUTPUT_PATH "${CMAKE_BINARY_DIR}")

# 包含子项目。
add_subdirectory ("QNTOOLS_CMAKE")
add_subdirectory ("qnusdtool")
add_subdirectory ("PostAssetUI")
add_subdirectory ("test")