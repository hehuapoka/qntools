# CMakeList.txt: CMakeProject 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#
cmake_minimum_required (VERSION 3.8)

# 将源代码添加到此项目的可执行文件。

add_compile_definitions(WIN32)
add_compile_definitions(USD_HAS_FULLSCREEN_SHADER=1)
add_compile_definitions(NOMINMAX)




set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


set(QNTOOLS $ENV{QNTools})
set(USD_ROOT ${QNTOOLS}/libs/USD)
set(PYTHONROOT $ENV{PYTHONROOT})


include_directories(${USD_ROOT}/include/boost-1_70)
include_directories(${USD_ROOT}/include)
include_directories(${PYTHONROOT}/include)

if(CMAKE_VERSION VERSION_LESS "3.7.0")
    set(CMAKE_INCLUDE_CURRENT_DIR ON)
endif()


link_directories(
    ${USD_DIR}/lib
)


add_library(qnusdtool SHARED 
    "Asset.cpp"
    "Asset.h"
    "importlib.h"
    "modelcheck.cpp"
    "modelcheck.h"
    "stagetool"
    "Submit.cpp"
    "Submit.h"
    "Utils.cpp"
    "Utils.h"
    )

target_link_libraries(qnusdtool ${USD_ROOT}/lib/boost_filesystem-vc142-mt-x64-1_70.lib
${USD_ROOT}/lib/boost_python37-vc142-mt-x64-1_70.lib
${USD_ROOT}/lib/usd_arch.lib
${USD_ROOT}/lib/usd_tf.lib
${USD_ROOT}/lib/usd_gf.lib
${USD_ROOT}/lib/usd_vt.lib
${USD_ROOT}/lib/usd_work.lib
${USD_ROOT}/lib/usd_ar.lib
${USD_ROOT}/lib/usd_kind.lib
${USD_ROOT}/lib/usd_sdf.lib
${USD_ROOT}/lib/usd_pcp.lib
${USD_ROOT}/lib/usd_usd.lib
${USD_ROOT}/lib/usd_usdGeom.lib
${USD_ROOT}/lib/usd_usdShade.lib
${USD_ROOT}/lib/usd_usdUtils.lib
${USD_ROOT}/lib/tbb.lib
${PYTHONROOT}/libs/python37.lib
)
# TODO: 如有需要，请添加测试并安装目标。
