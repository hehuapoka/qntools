cmake_minimum_required (VERSION 3.8)



set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_definitions(WIN32)
add_compile_definitions(USD_HAS_FULLSCREEN_SHADER=1)
add_compile_definitions(NOMINMAX)

set(QNTOOLS $ENV{QNTools})
set(USD_ROOT ${QNTOOLS}/libs/USD)
set(PYTHONROOT $ENV{PYTHONROOT})


include_directories(${USD_ROOT}/include/boost-1_70)
include_directories(${USD_ROOT}/include)
include_directories(${PYTHONROOT}/include)

include_directories(../qnusdtool)

add_library(qnusdtool_py SHARED
	main.cpp
)
add_dependencies(qnusdtool_py qnusdtool)
target_link_libraries(qnusdtool_py qnusdtool)
target_link_libraries(qnusdtool_py 
	${USD_ROOT}/lib/boost_filesystem-vc142-mt-x64-1_70.lib
	${USD_ROOT}/lib/boost_regex-vc142-mt-x64-1_70.lib
	${USD_ROOT}/lib/boost_python37-vc142-mt-x64-1_70.lib
)
set_target_properties(qnusdtool_py PROPERTIES SUFFIX ".pyd")