# CMakeList.txt: CMakeProject 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#
cmake_minimum_required (VERSION 3.8)

# 将源代码添加到此项目的可执行文件。

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_PREFIX_PATH $ENV{QNTOOLS}/libs/Qt)
set(Qt5_DIR $ENV{QNTOOLS}/libs/Qt/lib/cmake/Qt5)


set(QNTOOLS $ENV{QNTools})
set(USD_ROOT ${QNTOOLS}/libs/USD)




if(CMAKE_VERSION VERSION_LESS "3.7.0")
    set(CMAKE_INCLUDE_CURRENT_DIR ON)
endif()

find_package(Qt5 COMPONENTS Widgets REQUIRED)
find_package(Qt5 COMPONENTS Core REQUIRED)
find_package(Qt5 COMPONENTS Gui REQUIRED)


include_directories(CMAKE_CURRENT_SOURCE_DIR)

include_directories(${USD_ROOT}/include/boost-1_70)
include_directories(${USD_ROOT}/include)


add_executable(PostAssetUI
    main.cpp
    widget.cpp
    widget.h
    widget.ui
    "assetprocess.hpp" "work.h" "work.cpp" "EnvUtils.cpp" "EnvUtils.h")


target_link_libraries(PostAssetUI Qt5::Widgets)
target_link_libraries(PostAssetUI Qt5::Core)
target_link_libraries(PostAssetUI Qt5::Gui)
target_link_libraries(PostAssetUI ${USD_ROOT}/lib/boost_filesystem-vc142-mt-x64-1_70.lib)

add_dependencies(PostAssetUI qnusdtool)

# TODO: 如有需要，请添加测试并安装目标。
